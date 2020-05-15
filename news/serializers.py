from rest_framework import serializers

from news.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'link', 'creation_date', 'author']
        read_only_fields = ['author']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'creation_date', 'author', 'post']
        read_only_fields = ['author']