"""
Приложение api.
Сериализаторы для моделей категорий, жанров, названий произведений,
рецензий, комментариев.
"""
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий."""

    class Meta:
        exclude = ['id']
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для жанров."""

    class Meta:
        exclude = ['id']
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор для названий произведений."""
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для рецензий."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    score = serializers.IntegerField()
    title = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate(self, value):
        author = self.context['request'].user
        title_id = (self.context['request'].
                    parser_context['kwargs'].get('title_id'))
        title = get_object_or_404(
            Title,
            id=title_id
        )
        if (self.context['request'].method == 'POST'
                and title.reviews.filter(author=author).exists()):
            raise serializers.ValidationError(
                f'Отзыв на произведение {title.name} уже существует'
            )
        return value

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
