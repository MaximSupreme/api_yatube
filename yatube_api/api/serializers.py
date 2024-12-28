from rest_framework import serializers

from posts.models import Group, Post, Comment


class PostSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(read_only=True, required=False)
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'author', 'image',
            'group', 'pub_date', 'comments'
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(
        slug_field='id',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
