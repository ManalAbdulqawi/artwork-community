from django.contrib import admin

from .models import Artwork
from .models import Comment


# Register your models here.
@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'slug', 'size','created_on','artist')
    search_fields = ['title','size']
    list_filter = ('size','created_on')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Comment)