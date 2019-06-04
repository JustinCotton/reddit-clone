from .models import Post, Comment, User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post-detail',
        many=True,
        read_only=True
    )
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment-detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'posts', 'comments')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        many=False,
        read_only=True
    )
    class Meta:
        model = Post
        fields = ('id', 'created_at', 'title', 'picture', 'content', 'site_url', 'vote_total', 'user',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset = Post.objects.all()
    )
    # user = serializers.PrimaryKeyRelatedField(
    #     queryset = User.objects.all()
    # )
    class Meta:
        model = Comment
        fields = ('id', 'created_at', 'content', 'vote_total', 'post',)
