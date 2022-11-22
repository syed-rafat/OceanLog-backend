from cgitb import lookup
from rest_framework import serializers
from .models import Article, Author, Category, Tags, Images
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status



class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'coverImage', 'slug', 'author', 'date', 'category', 'tag', 'content')
        lookup_field = 'slug'
        extra_kwargs = {
            'author': {'read_only': True}
        }



class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'coverImage', 'slug', 'author',
                  'date', 'category', 'tag')

        extra_kwargs = {
            'author': {'allow_null': True}
        }


class AuthorSerializer(serializers.ModelSerializer):
    # articles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = ('name', 'profession', 'email', 'bio', 'picture', 'account')
        extra_kwargs = {
            'account': {'read_only': True}
        }



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
    profile = serializers.PrimaryKeyRelatedField(read_only=True)  #queryset=Author.objects.all()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'profile', 'email')
        #read_only_fields = ('is_active', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                                   password=validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = '__all__'

class UserArticleSerializer(serializers.ModelSerializer):

    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'articles')