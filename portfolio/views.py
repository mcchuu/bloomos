from django.shortcuts import render
from .models import Note, Photo, Track, GameActivity, Book
def lock_screen(request):
    return render(request, 'portfolio/moon.html')

def desktop_view(request):
    # Fetch data to populate the apps
    context = {
        'notes': Note.objects.all(),
        'photos': Photo.objects.all(),
        'tracks': Track.objects.all(),
        'games': GameActivity.objects.all(),
    }
    return render(request, 'portfolio/petals.html', context)

def xbox_view(request):
    # Fetch the games from the database to show in the app
    games = GameActivity.objects.all()
    return render(request, 'portfolio/xbox.html', {'games': games})

def spotify_view(request):
    # Fetch the tracks from the database
    tracks = Track.objects.all()
    return render(request, 'portfolio/spotify.html', {'tracks': tracks})

def photos_view(request):
    # Fetch photos grouped by year (ordered by year descending)
    photos = Photo.objects.all().order_by('-year')
    return render(request, 'portfolio/photos.html', {'photos': photos})

def notes_view(request):
    # Fetch all notes (latest first)
    notes = Note.objects.all()
    return render(request, 'portfolio/notes.html', {'notes': notes})

def files_view(request):
    # 'Files' in bloomOS usually acts as a directory for all content
    context = {
        'total_photos': Photo.objects.count(),
        'total_notes': Note.objects.count(),
        'total_tracks': Track.objects.count(),
        'recent_notes': Note.objects.all()[:5], # Show last 5 notes
    }
    return render(request, 'portfolio/files.html', context)

def goodreads_view(request):
    books = Book.objects.all()
    return render(request, 'portfolio/goodreads.html', {'books': books})