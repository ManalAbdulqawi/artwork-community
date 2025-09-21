from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArtworkList.as_view(), name='home'),
    path('artists/', views.ArtistsList.as_view(), name='artists_list'),
    path('artist/<int:artist_id>/artworks/', views.artist_artwork, name='artist_artwork'),
    path('myartwork/<int:user_id>/', views.my_artwork, name='my_artwork'),
    path('<slug:slug>/', views.artwork_detail, name='artwork_detail'),
    
    
]