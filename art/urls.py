from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArtworkList.as_view(), name='home'),
    path('<slug:slug>/', views.artwork_detail, name='artwork_detail'),

]