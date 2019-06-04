from rest_framework import viewsets
from .serializers import PostSerializer, UserSerializer
from .models import Post, Comment, User

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
