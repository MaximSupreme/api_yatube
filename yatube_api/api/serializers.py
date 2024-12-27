from rest_framework import serializers

from posts.models import Group, Post, Comment


class PostSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(read_only=True, required=False)
    image = serializers.ImageField(read_only=True, required=False)
    comments = serializers.StringRelatedField(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date', 'comments')
    
    def create(self, validated_data):
        if 'image' or 'group' not in self.initial_data:
            post = Post.objects.create(**validated_data)
            return post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='post.id')
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
