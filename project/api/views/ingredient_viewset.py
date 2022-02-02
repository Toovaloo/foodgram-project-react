from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import IngredientSerializer
from recipes.models import Ingredient


class IngredientViewset(viewsets.ViewSet):
    def list(self, request):
        query = request.query_params.get('query')
        ingredients = Ingredient.objects.filter(title__icontains=query)
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
