from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Artwork

# Create your views here.
class ArtworkList(generic.ListView):
    queryset = Artwork.objects.all()
    template_name = "art/index.html"

def artwork_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Artwork.objects.all()
    art = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "art/artwork_detail.html",
        {"art": art},
    )    
