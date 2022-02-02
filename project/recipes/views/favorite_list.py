from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from recipes.models import Recipe
from recipes.views.helpers import (get_paginator_and_page,
                                   get_tags_and_checked_tags)


@login_required
def favorite_list(request):
    '''
    Renders the list of user's favorites.
    '''
    tags, checked_tags = get_tags_and_checked_tags(request)
    favorite_ids = request.user.favorites.values_list('recipe__id', flat=True)
    favorite_recipes = Recipe.objects.filter(
        tags__in=checked_tags, id__in=favorite_ids,
    ).prefetch_related('author', 'tags').distinct()
    paginator, page = get_paginator_and_page(request, favorite_recipes)
    return render(
        request,
        'recipes/favorite.html',
        {
            'page': page,
            'paginator': paginator,
            'tags': tags,
            'checked_tags': checked_tags,
        },
    )
