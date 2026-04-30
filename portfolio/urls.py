from django.urls import path
from . import views

urlpatterns = [
    path('', views.lock_screen, name='lock_screen'),
    path('desktop/', views.desktop_view, name='desktop'),
    path('photos/', views.photos_view, name='photos'),
    path('notes/', views.notes_view, name='notes'),
    path('files/', views.files_view, name='files'),
    path('xbox/', views.xbox_view, name='xbox'),
    path('spotify/', views.spotify_view, name='spotify'),
    path('goodreads/', views.goodreads_view, name='goodreads'),
]