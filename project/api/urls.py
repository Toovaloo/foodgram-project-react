from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

router.register(
    r'ingredients', views.IngredientViewset, basename='ingredients')
router.register(
    r'purchases', views.PurchaseViewset, basename='purchases')
router.register(
    r'subscriptions', views.FollowViewset, basename='subscriptions')
router.register(
    r'favorites', views.FavoriteViewset, basename='favorites')

urlpatterns = [
    path('api/', include(router.urls)),
]
