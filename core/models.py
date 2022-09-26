from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# Create your models here.

class Author(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    bio = models.TextField()
    picture = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

    # def perform_create(self, request):
    #     self.account = request.auth.


class Category(models.Model):
    name = models.CharField(max_length=50)
    tags = models.ManyToManyField("Tags", related_name="categories")

    def __str__(self):
        return self.name



#tags or sub categories, multiple category can be under 1 tags and multiple tags can be under 1 category


class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    coverImage = models.ImageField(upload_to='images/', null=True, blank=True)
    img = CloudinaryField('image', overwrite=True, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    related_articles = models.ManyToManyField('self', blank=True)
    tag = models.ForeignKey("Tags", on_delete=models.CASCADE, related_name="articles")

    
    def Meta(self):
        ordering = ['-date']
    
    def save(self, *args, **kwargs):

        to_assign = slugify(self.title)

        if Article.objects.filter(slug=to_assign).exists():
            to_assign = to_assign + '-' + str(Article.objects.filter(slug=to_assign).count())

        self.slug = to_assign
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title