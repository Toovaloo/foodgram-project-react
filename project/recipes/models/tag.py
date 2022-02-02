from django.db import models


class Tag(models.Model):
    name = models.CharField(
        'тег',
        primary_key=True,
        max_length=200,
    )
    color = models.CharField(
        'цвет тега',
        max_length=50,
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        'тег (англ.)',
        max_length=200,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['name', 'slug']

    def __str__(self):
        return self.slug
