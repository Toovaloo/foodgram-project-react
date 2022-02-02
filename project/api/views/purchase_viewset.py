from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cart.cart import CartIsEmpty
from cart.models import Cart

User = get_user_model()


class PurchaseViewset(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        recipe_id = request.data.get('id')
        cart = request.cart
        try:
            cart.add(recipe_id)
        except Cart.DoesNotExist:
            return Response({'success': False})
        return Response({'success': True})

    def destroy(self, request, pk):
        cart = request.cart
        try:
            cart.remove(pk)
        except (Cart.DoesNotExist, CartIsEmpty):
            return Response({'success': False})
        return Response({'success': True})
