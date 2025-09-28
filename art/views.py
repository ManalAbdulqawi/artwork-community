from django.shortcuts import render,get_object_or_404,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Artwork,Comment
from .models import User
from django.utils.text import slugify

from .forms import CommentForm
from .forms import ArtworkForm
from .forms import ArtworkFormEdit
from .forms import ProfileFormEdit




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
    artwork_form_edit= ArtworkFormEdit()


    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.artist = request.user
            comment.artwork = art
            comment_count +=1
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
         "artwork_form_edit": artwork_form_edit,
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
    if request.method == "POST":
        artwork_form = ArtworkForm(request.POST, request.FILES)
        if artwork_form.is_valid():
            artwork = artwork_form.save(commit=False)
            title = artwork_form.cleaned_data['title']
            slug = slugify(title)
            artwork.slug = slug
            artwork.artist = request.user
            artwork.save()
            artworks_count += 1
            messages.add_message(
            request, messages.SUCCESS,
           'New Artwork submitted')
    artwork_form = ArtworkForm()

    return render(
        request,
        "art/my_artwork.html",
        {"artworks": artworks,
         "artworks_count":artworks_count,
         "artwork_form": artwork_form,},
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



def artwork_edit(request, slug):
    """
    view to edit artwork description and size
    """
    if request.method == "POST":

        queryset = Artwork.objects.all()
        art = get_object_or_404(queryset, slug=slug)
        #comment = get_object_or_404(Comment, pk=comment_id)
        artwork_form_edit = ArtworkFormEdit(data=request.POST, instance=art)

        if artwork_form_edit.is_valid() and art.artist == request.user:
            art = artwork_form_edit.save()
            messages.add_message(request, messages.SUCCESS, 'Artwork Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating artwork!')

    return HttpResponseRedirect(reverse('artwork_detail', args=[slug]))



def artwork_delete(request, slug):
    """
    view to edit artwork description and size
    """
    

    queryset = Artwork.objects.all()
    art = get_object_or_404(queryset, slug=slug)

    if art.artist == request.user:
        art.delete()
        messages.add_message(request, messages.SUCCESS, 'Artwork Deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Error Deleteing artwork!')

    return HttpResponseRedirect(reverse('my_artwork',args=[art.artist.id]))



def my_profile(request, user_id):
    queryset = User.objects.all()
    profile=get_object_or_404(queryset,id=user_id)
    if request.method == "POST":
        user_form = ProfileFormEdit(request.POST, instance=profile)
        if user_form.is_valid() and profile.id == request.user.id:
            profile = user_form.save()
            messages.add_message(
            request, messages.SUCCESS,
           'Your Profile Updated')
    user_form = ProfileFormEdit()
    return render(
        request,
        "art/my_profile.html",
        {"profile": profile,
         "user_form": user_form,},
    )