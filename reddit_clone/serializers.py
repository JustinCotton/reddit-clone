from .models import Post, Comment, User
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Post
        fields = ('id', 'created_at', 'title', 'picture', 'content', 'site_url', 'vote_total', 'user',)

            
