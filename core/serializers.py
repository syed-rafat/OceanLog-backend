from cgitb import lookup
from rest_framework import serializers
from .models import Article, Author, Category, Tags
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    related_articles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Article
        fields = '__all__'
        lookup_field = 'slug'


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'coverImage', 'slug', 'author',
                  'date', 'category', 'tag')


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


class RegisterSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'profile', 'name')

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                                   password=validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user
