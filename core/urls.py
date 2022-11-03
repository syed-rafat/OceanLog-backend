from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, ArticleViewSet, CategoryViewSet, TagViewSet, RegisterViewSet, ArticleList, ImageUrlview

router =  DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'user', RegisterViewSet)
# router.register(r'articlelist', ArticleListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list', ArticleList.as_view()),
    path('image/', ImageUrlview.as_view(), {'filename': 'img.jpg'}),
]
