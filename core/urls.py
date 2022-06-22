from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, ArticleViewSet

router =  DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
