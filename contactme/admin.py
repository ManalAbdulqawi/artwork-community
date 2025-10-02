from django.contrib import admin
from .models import ContactRequest


# Register your models here.
@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):

    list_display = ('subject','message', 'read',) 