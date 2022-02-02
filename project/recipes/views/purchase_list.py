from django.shortcuts import render


def purchase_list(request):
    '''
    Render the shopping list page.
    '''
    return render(
        request,
        'recipes/shop_list.html',
        {
            'cart': request.cart,
        }
    )
