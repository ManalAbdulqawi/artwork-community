from django.shortcuts import render
from django.views import generic
from .models import Artwork

# Create your views here.
class ArtworkList(generic.ListView):
    queryset = Artwork.objects.all()
    template_name = "artwork_list.html"

