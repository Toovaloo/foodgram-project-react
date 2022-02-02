def counter(request):
    '''
    Returns the current amount of recipes in user's shopping list.
    '''
    return {'counter': request.cart.count()}
