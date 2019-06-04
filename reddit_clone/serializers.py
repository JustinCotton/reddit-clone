from .models import Post, Comment, User                                                           
from rest_framework import serializers

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset = Post.objects.all()
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all()
    )
    class Meta:
        model = Commentfields = ('id', 'created_at', 'content', 'vote_total', 'user', 'post')