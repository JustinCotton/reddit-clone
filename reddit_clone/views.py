from rest_framework import viewsets
from .models import Post, Comment, USer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer