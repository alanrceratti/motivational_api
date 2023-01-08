from rest_framework import serializers

from .models import Category, Phrases


class PhrasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrases
        fields = ('id', 'category_name', 'phrase', 'image', 'image_url')


class CategorySerializer(serializers.ModelSerializer):
#   Nested relationship - mostra todas as frases dentro do endpoint categories
    phrases = PhrasesSerializer(many=True, read_only=True)

#   Hyperlinked Related Filed
    # phrases = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='phrases-detail')

    class Meta:
        model = Category
        fields = ('category_name', 'id', 'phrases')
