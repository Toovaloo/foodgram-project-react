from recipes.models import Ingredient

NAME_INGR = 'nameIngredient_'
VALUE_INGR = 'valueIngredient_'


def get_ingredients_from_request(request):
    '''
    Gets and validates ingredients from a request and returns the list.
    The query has the following structure:

    'nameIngredient_1': ['Яйцо'], 'valueIngredient_1': ['4'],
    'unitsIngredient_1': ['шт.']
    '''
    ingr_cnt = 0
    error_code = 0
    error_messages = []
    ingredients = []
    for field, value in request.POST.items():
        if field.find(NAME_INGR, 0) != -1:
            _, ingredient_order = field.split('_')
            amount = request.POST[VALUE_INGR + ingredient_order]
            if int(amount) < 0:
                error_code = 1
                error_messages.append(
                    'Количество ингредиентов не может быть отрицательным!')
                break
            ingredient = Ingredient.objects.get(title=value)
            ingredients.append((ingredient, amount))
            ingr_cnt += 1
    if ingr_cnt == 0:
        error_code = 1
        error_messages.append(
            'Вы должны добавить хотя бы один ингредиент!'
        )
    return {
        'error_code': error_code,
        'error_messages': error_messages,
        'ingredients': ingredients,
    }
