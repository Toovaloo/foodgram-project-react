from django.conf import settings
from django.core.paginator import Paginator


def get_paginator_and_page(request, object_list):
    '''
    Gets request and queryset and returns tuple(paginator, page).
    '''
    paginator = Paginator(object_list, settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return (paginator, page)
