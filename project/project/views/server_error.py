from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(7)
def server_error(request, exception=None):
    return render(request, 'misc/500.html', status=500)
