from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        'recipes.Recipe',
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name='рецепт',
    )
    ingredient = models.ForeignKey(
        'recipes.Ingredient',
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name='ингредиент',
    )
    amount = models.IntegerField(
        'количество',
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100000),
        ]
    )

    class Meta:
        verbose_name = 'рецепт-ингредиент'
        verbose_name_plural = 'рецепты-ингредиенты'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipeingredient',
            )
        ]

    def __str__(self):
        return f'{self.recipe.name}, {self.ingredient.title}, {self.amount}'

    def __repr__(self):
        return str(self)
