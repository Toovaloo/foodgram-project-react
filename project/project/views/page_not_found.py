from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(7)
def page_not_found(request, exception=None):
    return render(
        request, 'misc/404.html',
        {'path': request.path}, status=404
    )
