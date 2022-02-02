from django.urls import path

from about import views

urlpatterns = [
    path('author/', views.AboutAuthorView.as_view(), name='author'),
    path('technologies/', views.AboutTechView.as_view(), name='technologies'),
]
