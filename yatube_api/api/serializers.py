from rest_framework import serializers
from posts.models import Group, Post, Comment


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug')


class GroupSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description', 'posts')


class PostSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(read_only=True, required=False)
    image = serializers.ImageField(read_only=True, required=False)
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('text', 'author', 'image', 'group')
    
    def create(self, validated_data):
        if 'image' or 'group' not in self.initial_data:
            post = Post.objects.create(**validated_data)
            return post


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('author', 'post', 'text')
