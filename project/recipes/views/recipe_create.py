from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from recipes.forms import RecipeForm
from recipes.views.helpers import (get_ingredients_from_request,
                                   get_tags_from_request, save_ingredients)


@login_required
def recipe_create(request):
    '''
    Renders the page with recipe creation form and
    saves the passed ingredients separately.
    '''
    form = RecipeForm(
        request.POST or None, request.FILES or None, author=request.user)
    tags = get_tags_from_request(request)
    if request.method == 'GET':
        return render(
            request,
            'recipes/form_recipe.html',
            {
                'form': form,
                'tags': tags,
                'ingredients': [],
            },
        )
    elif request.method == 'POST':
        ingredients = get_ingredients_from_request(request)
        if form.is_valid() and ingredients['error_code'] == 0:
            form.instance.author = request.user
            recipe = form.save()
            save_ingredients(recipe, ingredients['ingredients'])
            recipe.save()
            return redirect(
                'recipe_view', recipe_id=recipe.id, slug=recipe.slug)
        return render(
            request,
            'recipes/form_recipe.html',
            {
                'form': form,
                'tags': tags,
                'ingredients': ingredients['ingredients'],
                'error_messages': ingredients['error_messages'],
            },
        )
