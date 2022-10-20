from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Author, Article, Category, Tags
from .serializers import ArticleListSerializer, ArticleSerializer, AuthorSerializer, CategorySerializer, TagSerializer, \
    RegisterSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from .pagination import HomePagination


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    pagination_class = None


class ArticleList(ListAPIView):
    allowed_methods = ['get']
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    pagination_class = HomePagination


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = None


# class SingleArticle(generics.RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
