from django.urls import include, path

from recipes import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('', include('api.urls')),
    path('users/<str:username>/', views.recipe_author, name='recipe_author'),
    path('recipes/<int:recipe_id>/', views.recipe_view, name='recipe_view'),
    path('recipes/<int:recipe_id>/<slug:slug>/',
         views.recipe_view, name='recipe_view'),
    path('recipes/<int:recipe_id>/<slug:slug>/edit/',
         views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:recipe_id>/<slug:slug>/delete/',
         views.recipe_delete, name='recipe_delete'),
    path('recipes/create/',
         views.recipe_create, name='recipe_create'),
    path('subscriptions/',
         views.subscription_list, name='subscription_list'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('shopping-list/', views.purchase_list, name='purchase_list'),
    path('shopping-list/download/',
         views.purchase_download, name='purchase_download'),
]
