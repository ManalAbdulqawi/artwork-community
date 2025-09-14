from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

SIZE = ((0, "Small"), (1, "Medium"),(2,"Large"))


# Create your models here.
class Artwork(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    artist = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    art_image = CloudinaryField('image')
    size = models.IntegerField(choices=SIZE, default=0)



