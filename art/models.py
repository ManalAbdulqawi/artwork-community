from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

SIZE = ((0, "Small"), (1, "Medium"),(2,"Large"))


# Create your models here.
class Artwork(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    artist = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="artworks")
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    art_image = CloudinaryField('image')
    size = models.IntegerField(choices=SIZE, default=0)
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title} | added by {self.artist}" 


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    artwork = models.ForeignKey('Artwork',on_delete=models.CASCADE,related_name="comments")
    artist = models.ForeignKey(User, on_delete=models.CASCADE,related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.artist}"  

 




