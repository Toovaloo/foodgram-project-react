from django import forms
from django.core.exceptions import ValidationError

from recipes.models import Recipe, Tag


class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        to_field_name='slug',
    )

    class Meta:
        model = Recipe
        fields = [
            'name',
            'image',
            'description',
            'tags',
            'cooking_time',
        ]

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name']
        recipes = Recipe.objects.filter(name=name, author=self.author)
        for recipe in recipes:
            if self.instance.name != recipe.name:
                raise ValidationError(
                    'У вас уже есть рецепт с таким названием!')
        return name
