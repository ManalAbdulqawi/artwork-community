from .models import Comment
from .models import Artwork
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

