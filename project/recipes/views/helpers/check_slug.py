from django.shortcuts import get_object_or_404, redirect

from recipes.models import Recipe


def check_slug(redirect_to):
    '''
    Suppose you have the following URL address:
    https://foodgram.com/recipes/<recipe_id>/<slug>/

    Call this decorator to ensure that a passed <slug> corresponds
    to <recipe_id> otherwise redirect to a URL address
    with correct recipe_id/slug relation.
    '''
    def actual_decorator(function):
        def wrapped(*args, **kwargs):
            recipe_id = kwargs.get('recipe_id')
            slug = kwargs.get('slug')
            recipe = get_object_or_404(Recipe, id=recipe_id)
            if slug is None or recipe.slug != slug:
                return redirect(
                    redirect_to, recipe_id=recipe.id, slug=recipe.slug)
            return function(*args, **kwargs)
        return wrapped
    return actual_decorator
