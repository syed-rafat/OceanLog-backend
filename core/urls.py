from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, ArticleViewSet, CategoryViewSet

router =  DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
