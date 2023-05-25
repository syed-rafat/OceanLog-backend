from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Author, Article, Category, Tags, Images
from .serializers import ArticleListSerializer, ArticleSerializer, AuthorSerializer, CategorySerializer, TagSerializer, RegisterSerializer, ImageSerializer, UserArticleSerializer
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .pagination import HomePagination
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    pagination_class = None
    # permission_classes = [IsAuthenticated]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    pagination_class = None
    permission_classes=[IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleList(ListAPIView):
    allowed_methods = ['get']
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    pagination_class = HomePagination


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = None
    # lookup_field = 'slug'
    # permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


# class SingleArticle(generics.RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class ImageUrlview(generics.CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    # permission_classes = [AllowAny]
    pagination_class = None

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(dir(request))
        print('             Rquest    Dictionary')
        print(request.__dict__)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        link = {"url": "https://res.cloudinary.com/dylqfbsq2/" + serializer.data['url']}
        print(serializer.data)
        print(link)
        return Response(link, status=200)


# Use this view to get username from accesstoken authorization
class UserInfoView(APIView):

    def get(self, request):
        user = request.user
        user_obj = User.objects.get(username=user)
        profile = {"id": user_obj.id,
        "username": user_obj.username}

        return Response(profile, status=200)


# To get all articles related to author, Use the UserArticleView by sending access token to get list 

class UserArticles(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)

        serializer = UserArticleSerializer(user)

        return Response(serializer.data, status=200)


class ArticleListByCategory(ListAPIView):
    serializer_class = ArticleListSerializer
    pagination_class = None

    def get_queryset(self):
        category = self.kwargs['category']
        return Article.objects.filter(category__id=category)