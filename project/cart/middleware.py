from django.utils.deprecation import MiddlewareMixin

from cart.cart import Cart


class CartMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.cart = Cart(request)
