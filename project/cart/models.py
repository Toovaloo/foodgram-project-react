from django.conf import settings
from django.db import models


class Cart(models.Model):
    customer = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='покупатель',
        null=True,
    )
    recipes = models.ManyToManyField(
        'recipes.Recipe',
        related_name='carts',
        verbose_name='рецепты',
    )
    creation_date = models.DateTimeField(
        'дата создания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
        ordering = ['-creation_date']

    def __str__(self):
        return (f"{self.customer}'s cart"
                if self.customer else f"Cart №{self.id}")
