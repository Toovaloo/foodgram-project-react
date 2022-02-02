from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from recipes.forms import RecipeForm
from recipes.models import Recipe, RecipeIngredient
from recipes.views.helpers import (check_slug, get_ingredients_from_request,
                                   get_tags_from_request, save_ingredients)


@check_slug('recipe_edit')
@login_required
def recipe_edit(request, recipe_id, slug=None):
    '''
    Renders the page with recipe edit form and
    saves edited/newly added ingredients separately.
    '''
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.author:
        return redirect('recipe_view', recipe_id=recipe_id, slug=recipe.slug)
    form = RecipeForm(
        request.POST or None,
        request.FILES or None,
        author=request.user,
        instance=recipe,
    )
    if request.method == 'GET':
        tags = recipe.tags.all()
        rec_ingrs = recipe.recipe_ingredients.prefetch_related('ingredient')
        ingredients = [
            (rec_ingr.ingredient, rec_ingr.amount) for rec_ingr in rec_ingrs]
        return render(
            request,
            'recipes/form_recipe.html',
            {
                'form': form,
                'tags': tags,
                'recipe': recipe,
                'ingredients': ingredients,
            },
        )
    elif request.method == 'POST':
        tags = get_tags_from_request(request)
        ingredients = get_ingredients_from_request(request)
        if form.is_valid() and ingredients['error_code'] == 0:
            recipe = form.save()
            # delete old recipe's ingredients
            RecipeIngredient.objects.filter(recipe=recipe).delete()
            save_ingredients(recipe, ingredients['ingredients'])
            recipe.save()
            return redirect(
                'recipe_view', recipe_id=recipe_id, slug=recipe.slug)
        return render(
            request,
            'recipes/form_recipe.html',
            {
                'form': form,
                'tags': tags,
                'recipe': recipe,
                'ingredients': ingredients['ingredients'],
                'error_messages': ingredients['error_messages'],
            },
        )
