from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# TODO: add description field to article model
# TODO: fix the image related problems in article model
# TODO: need to redo models according to ckeditor5

# NOTE: We are still using User as foreignkey for author in Article Model. Need to change it to Author model 


# Custom user model
# class AuthUser(User):
#     class Meta:
#         proxy = True

#     def __str__(self):
#         if hasattr(self, 'profile'):
#             print('has profile', self.profile.name)
#             return self.profile.name
        

class Author(models.Model):
    """
    Linked to django auth class User with account field
    """

    account = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    bio = models.TextField(blank=True)
    picture = CloudinaryField('image', overwrite=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_author_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(account=instance)


# tags or sub categories, multiple category can be under 1 tags and multiple tags can be under 1 category
class Category(models.Model):
    name = models.CharField(max_length=50)
    tags = models.ManyToManyField("Tags", related_name="categories")

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Images(models.Model):
    """
    Model which stores all the image, then linked to other model.
    url for this specific account is
     access url =   "https://res.cloudinary.com/dylqfbsq2/" + url from model

    Currently, images are not tied to article model, so their url link is only stored in html of article content for now.

    """

    url = CloudinaryField("image", overwrite="true")
    #No. of image


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    coverImage = CloudinaryField('image', overwrite=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    date = models.DateField(auto_now_add=True)
    content_text = models.TextField(blank=True, null=True)     #stores only text content from rich text editor
    content = models.TextField(blank=True, null=True)          #stores html content from rich text editor
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='articles')
    related_articles = models.ManyToManyField('self', blank=True)
    tag = models.ForeignKey("Tags", on_delete=models.DO_NOTHING, related_name="articles")

    def Meta(self):
        ordering = ['-date']

    def save(self, *args, **kwargs):
        to_assign = slugify(self.title)

        if Article.objects.filter(slug=to_assign).exists():
            to_assign = to_assign + '-' + str(Article.objects.filter(slug=to_assign).count())

        self.slug = to_assign
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)