from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from recipes.models import Recipe
from recipes.views.helpers import check_slug


@check_slug('recipe_delete')
@login_required
def recipe_delete(request, recipe_id, slug):
    '''
    Deletes the specified recipe if the user has such permissions.
    '''
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.author:
        return redirect('recipe_view', recipe_id=recipe_id, slug=recipe.slug)
    recipe.delete()
    return redirect('recipe_list')
