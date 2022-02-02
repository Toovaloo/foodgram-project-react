from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render

from recipes.models import Recipe
from recipes.views.helpers import (get_paginator_and_page,
                                   get_tags_and_checked_tags)

User = get_user_model()


def recipe_author(request, username):
    '''
    Renders the page with author's recipes.
    '''
    author = get_object_or_404(User, username=username)
    tags, checked_tags = get_tags_and_checked_tags(request)
    recipes = Recipe.objects.prefetch_related('author', 'tags').filter(
        author=author, tags__in=checked_tags).distinct()
    paginator, page = get_paginator_and_page(request, recipes)
    return render(
        request,
        'recipes/author_recipe.html',
        {
            'page': page,
            'paginator': paginator,
            'tags': tags,
            'checked_tags': checked_tags,
            'author': author,
        }
    )
