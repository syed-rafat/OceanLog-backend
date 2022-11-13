from cgitb import lookup
from rest_framework import serializers
from .models import Article, Author, Category, Tags, Images
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

    class Meta:
        model = Author
        fields = ('id', 'name', 'profession', 'email', 'bio', 'picture', 'articles', 'account')
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