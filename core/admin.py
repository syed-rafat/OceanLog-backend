from django.contrib import admin
from .models import Author, Article, Category, Tags, Images

# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Images)