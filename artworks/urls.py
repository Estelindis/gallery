from django.urls import path
from . import views

urlpatterns = [
    path('curate/', views.curate, name='curate'),
    # artists
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('artist/add/', views.add_artist, name='add_artist'),
    path(
        'artist/edit/<int:artist_id>/',
        views.edit_artist,
        name='edit_artist'),
    # designs
    path('designs/', views.all_designs, name='designs'),
    path('designs/add/', views.add_design, name='add_design'),
    path(
        'designs/edit/<int:design_id>/',
        views.edit_design,
        name='edit_design'),
    # canvasses
    path('canvasses/', views.all_canvasses, name='canvasses'),
    path('canvasses/add/', views.add_canvas, name='add_canvas'),
    path(
        'canvasses/edit/<int:canvas_id>/',
        views.edit_canvas,
        name='edit_canvas'),
    # artworks
    path('', views.all_artworks, name='artworks'),
    path('<int:artwork_id>/', views.artwork_detail, name='artwork_detail'),
    path('add/', views.add_artwork, name='add_artwork'),
    path('edit/<int:artwork_id>/', views.edit_artwork, name='edit_artwork'),
    path(
        'delete/<int:artwork_id>/',
        views.delete_artwork,
        name='delete_artwork'),
]
