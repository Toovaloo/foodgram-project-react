from recipes.models import RecipeIngredient

NAME_INGR = 'nameIngredient_'
VALUE_INGR = 'valueIngredient_'


def save_ingredients(recipe, ingredients):
    '''
    Saves passed ingredients.
    '''
    for ingredient in ingredients:
        rec_ingr, created = RecipeIngredient.objects.get_or_create(
            ingredient=ingredient[0],
            recipe=recipe,
        )
        if created:
            rec_ingr.amount = int(ingredient[1])
        else:
            rec_ingr.amount += int(ingredient[1])
        rec_ingr.save()
