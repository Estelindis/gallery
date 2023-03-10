from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_artworks, name='artworks'),
    path('<artwork_id>', views.artwork_detail, name='artwork_detail'),
    path('designs/', views.all_designs, name='designs'),
    path('canvasses/', views.all_canvasses, name='canvasses'),
]
