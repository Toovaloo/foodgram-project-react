from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import FavoriteSerializer
from recipes.models import Favorite


class FavoriteViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        recipe_id = request.data.get('id')
        serializer = FavoriteSerializer(
            data={'user': request.user, 'recipe': recipe_id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True})

    def destroy(self, request, pk):
        favorite = get_object_or_404(
            Favorite, user=request.user, recipe__id=pk)
        favorite.delete()
        return Response({'success': True})
