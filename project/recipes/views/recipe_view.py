from django.shortcuts import get_object_or_404, render

from recipes.models import Recipe
from recipes.views.helpers import check_slug


@check_slug('recipe_view')
def recipe_view(request, recipe_id, slug=None):
    '''
    Renders the page with detailed information about a specific recipe.
    '''
    recipe = get_object_or_404(Recipe, id=recipe_id)
    tags = recipe.tags.all()
    recipe_ingredient = recipe.recipe_ingredients.all()
    return render(
        request,
        'recipes/single_page.html',
        {
            'author': recipe.author,
            'recipe': recipe,
            'tags': tags,
            'recipe_ingredient': recipe_ingredient,
        }
    )
