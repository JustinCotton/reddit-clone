from .models import User
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
        fields = ('id', 'username', 'email', 'password', 'posts','comments',)