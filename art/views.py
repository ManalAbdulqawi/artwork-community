from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Artwork, Comment
from .models import User
from django.utils.text import slugify
from .forms import CommentForm
from .forms import ArtworkForm
from .forms import ArtworkFormEdit
from .forms import ProfileFormEdit
# Create your views here.


class ArtworkList(generic.ListView):
    """
    Returns all published Artwork in :model:`art.Artwork`
    and displays them in a long scrolled page. 
    **Context**

    ``queryset``
        All instances of :model:`art.Artwork`

    **Template:**

    :template:`art/index.html`

    """
    queryset = Artwork.objects.all()
    template_name = "art/index.html"


class ArtistsList(generic.ListView):
    queryset = User.objects.filter(id__in=Artwork.objects.values_list('artist', flat=True).distinct()).order_by("username")
    template_name = "art/artists_list.html"  


def artwork_detail(request, slug):
    """
    Display an individual :model:`art.Artwork`.

    **Context**

    ``art``
        An instance of :model:`art.Artwork`.
    ``comments``
        All comments related to the art.
    ``comment_count``
        A count of comments related to the art.
    ``comment_form``
        An instance of :form:`art.CommentForm`
    ``artwork_form_edit``
        An instance of :form:`art.ArtworkFormEdit`

    **Template:**

    :template:`art/artwork_detail.html`

    """
    queryset = Artwork.objects.all()
    art = get_object_or_404(queryset, slug=slug)
    comments = art.comments.all().order_by("-created_on")
    comment_count = art.comments.count()
    artwork_form_edit = ArtworkFormEdit()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.artist = request.user
            comment.artwork = art
            comment_count +=1
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment submitted')

    comment_form = CommentForm()
    return render(
        request,
        "art/artwork_detail.html",
        {"art": art,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
         "artwork_form_edit": artwork_form_edit,
         },)    


def artist_artwork(request, artist_id):

    """
    Returns all an artist's artwork in :model:`art.Artwork`
    and displays them in a long scrolled page. 

    **Context**

    ``artorks``
        All instances of an artist's artwork :model:`art.Artwork`
    ``artist``  
        An artist instance  :model:`art.auth.User`

    **Template:**

    :template:`art/artist_artwork.html`

    """
    artworks = Artwork.objects.filter(artist=artist_id)
    artist = User.objects.get(id=artist_id)
    return render(
        request,
        "art/artist_artwork.html",
        {"artworks": artworks,
         "artist": artist},
    )


def my_artwork(request, user_id):

    """
    Returns all login artist's artwork in :model:`art.Artwork`
    and displays them in a long scrolled page with a form to add new artwork.

     **Context**
    ``artworks``
        All artorks of login artist :model:`art.Artwork`.

    ``artworks_count``
        A count of artworks related to the login artist.

    ``artwork_form``
        An instance of :form:`art.ArtworkForm`
    ``artwork_form_edit``
        An instance of :form:`art.ArtworkFormEdit`

    **Template:**

    :template:`art/my_artwork.html`

    """
 
    artworks = Artwork.objects.filter(artist=user_id)
    artworks_count = artworks.filter(artist=user_id).count()
    artist=user_id
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
         "artworks_count": artworks_count,
         "artwork_form": artwork_form, 
         "artist": artist,} ,)


def comment_edit(request, slug, comment_id):

    """
    Display an individual comment for edit.

    **Context**

    ``art``
        An instance of :model:`art.Artwork`.
    ``comment``
        A single comment related to the art.
    ``comment_form``
        An instance of :form:`art.CommentForm`
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
    Delete an individual comment.

    **Context**

    ``art``
        An instance of :model:`art.Artwork`.
    ``comment``
        A single comment related to the art.
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
    Edit an individual Artworkm of login artist.

    **Context**

    ``art``
        An instance of :model:`art.Artwork`.
    ``artwork_form_edit``
        An instance of :form:`art.ArtworkFormEdit`.

    """
    if request.method == "POST":

        queryset = Artwork.objects.all()
        art = get_object_or_404(queryset, slug=slug)
        artwork_form_edit = ArtworkFormEdit(data=request.POST, instance=art)

        if artwork_form_edit.is_valid() and art.artist == request.user:
            art = artwork_form_edit.save()
            messages.add_message(request, messages.SUCCESS, 'Artwork Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating artwork!')

    return HttpResponseRedirect(reverse('artwork_detail', args=[slug]))



def artwork_delete(request, slug):
    """
    Delete an individual Artworkm of login artist.

    **Context**

    ``art``
        An instance of :model:`art.Artwork`.

    """
    queryset = Artwork.objects.all()
    art = get_object_or_404(queryset, slug=slug)

    if art.artist == request.user:
        art.delete()
        messages.add_message(request, messages.SUCCESS, 'Artwork Deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Error Deleteing artwork!')

    return HttpResponseRedirect(reverse('my_artwork', args=[art.artist.id]))


def my_profile(request, user_id):

    """
    Returns an artist details :model:`art.auth.User`
    to add artist's first name, last name and email if these are not exist. 

    **Context**

    ``queryset``
        All artists :model:`art.auth.User`
    ``profile``  
        An artist instance  :model:`art.auth.User`
    ``user_form``
        An instance of :form:`art.ProfileFormEdit`.

    **Template:**

    :template:`art/my_profile.html`

    """
    queryset = User.objects.all()
    profile = get_object_or_404(queryset,id=user_id)
    if request.method == "POST":
        user_form = ProfileFormEdit(request.POST, instance=profile)
        if user_form.is_valid() and profile.id == request.user.id:
            profile = user_form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Your Profile Updated')
    user_form = ProfileFormEdit()
    return render(
        request,
        "art/my_profile.html",
        {"profile": profile,
         "user_form": user_form, }, )
