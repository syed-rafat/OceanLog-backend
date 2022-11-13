from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Author, Article, Category, Tags, Images
from .serializers import ArticleListSerializer, ArticleSerializer, AuthorSerializer, CategorySerializer, TagSerializer, RegisterSerializer, ImageSerializer
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from .pagination import HomePagination
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated

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
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        print(self.request.user)
        print(self)
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


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated]


# This Apiview for image upload is not working so i implemented a a generic view down below  which is now working 

# class ImageUrlview(APIView):
#     # renderer_classes = [JSONRenderer]
#     parser_classes = (FileUploadParser,)

#     # def get(self, request, *args, **kwargs):
#     #     pk = self.kwargs['pk']
#     #     img = Images.objects.get(pk=pk)
#     #     image_link = "https://res.cloudinary.com/dylqfbsq2/" + str(img.url)
#     #     link = {'url': image_link}
#     #     return Response(link)

#     def post(self, request, filename, format=None):
#         print('self')
#         repr(self)
#         print('request')
#         print(request.data)
#         file = request.data['file']
#         serializer = ImageSerializer(data=request.data)
#         img_obj = Images.objects.create(url=file)
        
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#         link = {'url': str(img_obj.url)}
#         return Response(link)


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