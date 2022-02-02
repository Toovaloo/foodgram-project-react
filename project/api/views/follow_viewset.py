from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import FollowSerializer
from recipes.models import Follow

User = get_user_model()


class FollowViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        author_id = request.data.get('id')
        author = get_object_or_404(User, id=author_id)
        serializer = FollowSerializer(
            data={'author': author, 'subscriber': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True})

    def destroy(self, request, pk):
        follow = get_object_or_404(
            Follow, author__id=pk, subscriber=request.user)
        follow.delete()
        return Response({'success': True})
