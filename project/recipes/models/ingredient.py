from django.db import models


class Ingredient(models.Model):
    title = models.CharField(
        'название',
        max_length=200
    )
    dimension = models.CharField(
        'единицы измерения',
        max_length=200
    )

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'
        ordering = ['title']

    def __str__(self):
        return self.title
