from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from recipes import models

User = get_user_model()


class MyUserAdmin(UserAdmin):
    list_filter = UserAdmin.list_filter + ('username', 'email')


class RecipeAdmin(admin.ModelAdmin):
    list_filter = ('name',)


class IngredientAdmin(admin.ModelAdmin):
    list_filter = ('title',)


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.RecipeIngredient)
admin.site.register(models.Tag)
admin.site.register(models.Follow)
admin.site.register(models.Favorite)
