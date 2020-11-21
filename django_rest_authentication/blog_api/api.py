from .models import Post
from rest_framework import viewsets, permissions
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permissions_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
