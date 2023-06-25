from cgitb import lookup
from rest_framework import serializers
from .models import Article, Author, Category, Tags, Images
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


# serializer for registration view
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
        # password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class AuthorSerializer(serializers.ModelSerializer):
    # articles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = '__all__'
        extra_kwargs = {
            'account': {'read_only': True}
        }



class UserSerializer(serializers.ModelSerializer):

    profile = AuthorSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'profile')


class ArticleListSerializer(serializers.ModelSerializer):
    # author_name = serializers.StringRelatedField()
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'coverImage', 'slug', 'author',
                  'date', 'category', 'tag')

        extra_kwargs = {
            'author': {'allow_null': True}
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author_name'] = instance.author.profile.name
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True, required=False)
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),many=True)

    class Meta:
        model = Tags
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField(read_only=True)
    author = UserSerializer()
    tag = TagSerializer()


    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'coverImage', 'slug', 'author', 'date', 'category', 'tag', 'content')
        lookup_field = 'slug'
        extra_kwargs = {
            'author': {'read_only': True}
        }


class UserArticleSerializer(serializers.ModelSerializer):

    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'articles')

