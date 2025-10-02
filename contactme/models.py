from django.db import models

# Create your models here.

class ContactRequest(models.Model):
    """
    Stores a single collaboration request message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact request from {self.name}"    