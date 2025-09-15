from django.contrib import admin

from .models import Artwork
from .models import Comment


# Register your models here.
admin.site.register(Artwork)
admin.site.register(Comment)