from cgitb import lookup
from rest_framework import serializers
from .models import Article, Author, Category, Tags


class ArticleSerializer(serializers.ModelSerializer):
    related_articles  = serializers.StringRelatedField(many=True)
    class Meta:
        model = Article
        fields = '__all__'
        lookup_field = 'slug'

class AuthorSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True)
    account = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Author
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'



class TagSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Tags
        fields = '__all__'

