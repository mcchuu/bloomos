from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    body = models.TextField()
    is_locked = models.BooleanField(default=False, help_text='Lock this note behind a password for visitors.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        lock = ' 🔒' if self.is_locked else ''
        return f'{self.title}{lock}'


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=300, blank=True)
    year = models.IntegerField(help_text='Year this photo was taken (used for gallery grouping).')
    is_favorite = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year', '-uploaded_at']
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        fav = ' ♡' if self.is_favorite else ''
        return f'{self.year} — {self.caption or "untitled"}{fav}'


class Track(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200, blank=True)
    album_art = models.ImageField(upload_to='album_art/', blank=True, null=True)
    order = models.IntegerField(default=0, help_text='Controls display order in the playlist.')

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Track'
        verbose_name_plural = 'Playlist'

    def __str__(self):
        return f'{self.title} — {self.artist}'


class GameActivity(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='game_covers/', blank=True, null=True)
    hours_played = models.FloatField(default=0.0, help_text='Total hours played.')
    achievements_earned = models.IntegerField(default=0)
    achievements_total = models.IntegerField(default=0, help_text='Total possible achievements for this game.')

    class Meta:
        ordering = ['-hours_played']
        verbose_name = 'Game'
        verbose_name_plural = 'Game Activity'

    def __str__(self):
        return self.title

    def completion_percentage(self):
        if self.achievements_total == 0:
            return 0
        return round((self.achievements_earned / self.achievements_total) * 100, 1)
    completion_percentage.short_description = 'Completion %'
