from .models import ContactRequest
from django import forms

class ContactRequestForm(forms.ModelForm):
    class Meta:
        model= ContactRequest
        fields = ('name', 'email','subject', 'message')