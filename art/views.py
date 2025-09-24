from django.shortcuts import render,get_object_or_404,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Artwork,Comment
from .models import User
from .forms import CommentForm



# Create your views here.
class ArtworkList(generic.ListView):
    queryset = Artwork.objects.all()
    template_name = "art/index.html"

    


class ArtistsList(generic.ListView):
    queryset = User.objects.filter(id__in=Artwork.objects.values_list('artist', flat=True).distinct()).order_by("username")
    template_name = "art/artists_list.html"  

def artwork_detail(request, slug):
    """
    
    """

    queryset = Artwork.objects.all()
    art = get_object_or_404(queryset, slug=slug)
    comments = art.comments.all().order_by("-created_on")
    comment_count = art.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.artist = request.user
            comment.artwork = art
            comment.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted'
    )

    comment_form = CommentForm()


    return render(
        request,
        "art/artwork_detail.html",
        {"art": art,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
},
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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Artwork.objects.all()
        art = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.artist == request.user:
            comment = comment_form.save(commit=False)
            comment.artwork = art
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('artwork_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Artwork.objects.all()
    art = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.artist == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('artwork_detail', args=[slug]))