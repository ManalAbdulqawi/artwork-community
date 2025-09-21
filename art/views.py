from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Artwork
from .models import User


# Create your views here.
class ArtworkList(generic.ListView):
    queryset = Artwork.objects.all()
    template_name = "art/index.html"

    


class ArtistsList(generic.ListView):
    queryset = User.objects.filter(id__in=Artwork.objects.values_list('artist', flat=True).distinct())
    template_name = "art/artists_list.html"  

def artwork_detail(request, slug):
    """
    
    """

    queryset = Artwork.objects.all()
    art = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "art/artwork_detail.html",
        {"art": art},
    )    

def artist_artwork(request, artist_id):
    artworks = Artwork.objects.filter(artist=artist_id)
    artist = User.objects.get(id=artist_id)
    return render(
        request,
        "art/artist_artwork.html",
        {"artworks": artworks,
         "artist": artist},
    )

def my_artwork(request, user_id):
    artworks = Artwork.objects.filter(artist=user_id)
    artworks_count = artworks.filter(artist=user_id).count()
    return render(
        request,
        "art/my_artwork.html",
        {"artworks": artworks,
         "artworks_count":artworks_count,},
    )

