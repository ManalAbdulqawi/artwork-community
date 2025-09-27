from .models import Comment
from .models import Artwork
from .models import User

from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields =('title','description','art_image','size',)


class ArtworkFormEdit(forms.ModelForm):
    class Meta:
        model = Artwork
        fields =('description',)

class ProfileFormEdit(forms.ModelForm):
    class Meta:
        model = User
        fields =('email','first_name','last_name')

