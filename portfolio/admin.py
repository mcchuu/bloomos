from django.contrib import admin
from django.utils.html import format_html
from .models import Note, Photo, Track, GameActivity, Book

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_locked', 'updated_at', 'created_at')
    list_filter = ('is_locked', 'owner')
    search_fields = ('title', 'body')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_locked',)
    ordering = ('-updated_at',)

    fieldsets = (
        ('Note Content', {
            'fields': ('owner', 'title', 'body')
        }),
        ('Settings', {
            'fields': ('is_locked',),
            'description': 'Locked notes are hidden behind a password prompt for visitors.'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'caption', 'year', 'owner', 'is_favorite', 'uploaded_at')
    list_filter = ('year', 'is_favorite', 'owner')
    search_fields = ('caption',)
    list_editable = ('is_favorite',)
    ordering = ('-year', '-uploaded_at')

    fieldsets = (
        ('Photo', {
            'fields': ('owner', 'image', 'caption')
        }),
        ('Details', {
            'fields': ('year', 'is_favorite'),
            'description': 'Year is used to group photos in the gallery by year.'
        }),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:50px; width:50px; object-fit:cover; border-radius:4px;" />',
                obj.image.url
            )
        return '—'
    thumbnail.short_description = 'Preview'


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album', 'order', 'album_art_preview', 'owner')
    list_display_links = ('title',)
    list_filter = ('artist', 'owner')
    search_fields = ('title', 'artist', 'album')
    list_editable = ('order',)
    ordering = ('order',)

    fieldsets = (
        ('Track Info', {
            'fields': ('owner', 'title', 'artist', 'album', 'album_art')
        }),
        ('Playlist Order', {
            'fields': ('order',),
            'description': 'Lower numbers appear first in the playlist.'
        }),
    )

    def album_art_preview(self, obj):
        if obj.album_art:
            return format_html(
                '<img src="{}" style="height:40px; width:40px; object-fit:cover; border-radius:4px;" />',
                obj.album_art.url
            )
        return '—'
    album_art_preview.short_description = 'Art'


@admin.register(GameActivity)
class GameActivityAdmin(admin.ModelAdmin):
    list_display = ('cover_preview', 'title', 'hours_played', 'achievements_earned', 'achievements_total', 'completion_percentage', 'owner')
    list_filter = ('owner',)
    search_fields = ('title',)
    ordering = ('-hours_played',)

    fieldsets = (
        ('Game', {
            'fields': ('owner', 'title', 'cover')
        }),
        ('Stats', {
            'fields': ('hours_played', 'achievements_earned', 'achievements_total'),
            'description': 'Completion percentage is calculated automatically from achievements earned vs total.'
        }),
    )

    def cover_preview(self, obj):
        if obj.cover:
            return format_html(
                '<img src="{}" style="height:50px; width:40px; object-fit:cover; border-radius:4px;" />',
                obj.cover.url
            )
        return '—'
    cover_preview.short_description = 'Cover'

    def completion_percentage(self, obj):
        pct = obj.completion_percentage()
        if pct >= 75:
            color = '#28a745'
        elif pct >= 40:
            color = '#fd7e14'
        else:
            color = '#6c757d'
        return format_html(
            '<span style="color:{}; font-weight:600;">{}%</span>',
            color, pct
        )
    completion_percentage.short_description = 'Complete'

# portfolio/admin.py

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Remove 'status' from these two lists:
    list_display = ('title', 'author', 'status')  # Change to ('title', 'author')
    list_filter = ('status',)                     # Delete this line or change to ('author',)