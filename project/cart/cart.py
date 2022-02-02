import logging
from io import BytesIO

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

from cart import models
from recipes.models import Recipe, RecipeIngredient

logger = logging.getLogger(__name__)


class CartIsEmpty(Exception):
    '''
    Occurs when you're trying to remove an item from an empty cart.
    '''
    pass


class Cart:
    def __init__(self, request):
        self.request = request
        cart_id = request.session.get(settings.CART_ID)
        user = request.user if request.user.is_authenticated else None
        if user:
            try:
                cart = models.Cart.objects.get(customer=user)
            except models.Cart.DoesNotExist:
                cart = self.get(id=cart_id)
                cart.customer = user
                cart.save()
            self.append(cart, cart_id)
            request.session[settings.CART_ID] = cart.id
        else:
            cart = self.get(id=cart_id)
        self.cart = cart

    def __iter__(self):
        for recipe in self.cart.recipes.all():
            yield recipe

    def __contains__(self, item):
        for recipe in self:
            if recipe == item:
                return True
        return False

    def get(self, *args, **kwargs):
        '''
        Responsible for extracting object from database and
        exception handling.
        '''
        try:
            cart = models.Cart.objects.get(*args, **kwargs)
        except models.Cart.DoesNotExist:
            cart = self.new(self.request)
        return cart

    def new(self, request):
        cart = models.Cart.objects.create()
        if request.user.is_authenticated:
            cart.customer = request.user
            cart.save()
        request.session[settings.CART_ID] = cart.id
        return cart

    def add(self, recipe_id):
        '''
        Raises Cart.DoesNotExist if no recipe was found.

        There's no exception handling because the view should respond
        to a request accordingly with operation success=True/False.
        '''
        recipe = Recipe.objects.get(id=recipe_id)
        self.cart.recipes.add(recipe)
        self.cart.save()

    def remove(self, recipe_id):
        '''
        Raises Cart.DoesNotExist if no recipe was found
        or CartIsEmpty if there were no recipes in cart.

        There's no exception handling because the view should respond
        to a request accordingly with operation success=True/False.
        '''
        if self.is_empty:
            raise CartIsEmpty
        recipe = self.cart.recipes.get(id=recipe_id)
        self.cart.recipes.remove(recipe)
        self.cart.save()

    def append(self, cart_model, cart_id):
        '''
        Appends all items from anonym's cart to logged in user's.
        '''
        if not cart_model.id == cart_id:
            try:
                old_cart = models.Cart.objects.get(id=cart_id)
            except ObjectDoesNotExist:
                logger.info(f'Cart object with id={cart_id} not found.')
            else:
                for recipe in old_cart.recipes.all():
                    cart_model.recipes.add(recipe)
                # delete anonym's cart after you appended all items from it
                # to the currently logged in user's cart
                old_cart.delete()

    def count(self):
        return self.cart.recipes.count()

    def clear(self):
        self.cart.recipes.all().delete()

    @property
    def is_empty(self):
        return self.count() == 0

    def _convert_to_dict(self):
        converted = {}
        rec_ingrs = RecipeIngredient.objects.filter(
            recipe__in=self.cart.recipes.all()).prefetch_related(
                'recipe', 'ingredient').all()
        for rec_ingr in rec_ingrs:
            try:
                converted[rec_ingr.ingredient.title][1] += rec_ingr.amount
            except KeyError:
                converted[rec_ingr.ingredient.title] = [
                    f'{rec_ingr.ingredient.dimension}', rec_ingr.amount]
        return converted

    def convert_to_pdf(self):
        x, y = 20, 40
        converted = self._convert_to_dict()
        buffer = BytesIO()
        canvas = Canvas(buffer, bottomup=0)
        pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
        canvas.setFont('DejaVuSans', 28)
        canvas.drawString(x, y, 'Список покупок')
        for key, value in converted.items():
            line = '• ' + key + ' (' + value[0] + ') — ' + str(value[1])
            y += 40
            canvas.drawString(x, y, line)
            if y >= 800:
                y = 40
                canvas.showPage()
                canvas.setFont('DejaVuSans', 28)
        canvas.save()
        pdf = buffer.getvalue()
        buffer.close()
        return pdf
