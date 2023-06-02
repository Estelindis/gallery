from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_artworks, name='artworks'),
    path('<int:artwork_id>/', views.artwork_detail, name='artwork_detail'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('designs/', views.all_designs, name='designs'),
    path('canvasses/', views.all_canvasses, name='canvasses'),
    path('add/', views.add_artwork, name='add_artwork'),
    path('edit/<int:artwork_id>/', views.edit_artwork, name='edit_artwork'),
    path(
        'delete/<int:artwork_id>/',
        views.delete_artwork,
        name='delete_artwork'),
    path('artist/add/', views.add_artist, name='add_artist'),
    path(
        'artist/edit/<int:artist_id>/',
        views.edit_artist,
        name='edit_artist'),
    path(
        'artist/delete/<int:artist_id>/',
        views.delete_artist,
        name='delete_artist'),
]
