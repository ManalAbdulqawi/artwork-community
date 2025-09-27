from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArtworkList.as_view(), name='home'),
    path('artists/', views.ArtistsList.as_view(), name='artists_list'),
    path('artist/<int:artist_id>/artworks/', views.artist_artwork, name='artist_artwork'),
    path('myartwork/<int:user_id>/', views.my_artwork, name='my_artwork'),
    path('myprofile/<int:user_id>/', views.my_profile, name='my_profile'),
    path('<slug:slug>/', views.artwork_detail, name='artwork_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'), 
    path('<slug:slug>/edit_artwork/',
         views.artwork_edit, name='artwork_edit'),  
    path('<slug:slug>/delete_artwork/',
         views.artwork_delete, name='artwork_delete'),         
    
    
]