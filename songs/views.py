# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Song

# Create your views here.

def index(request):
    """Home page"""
    return render(request, 'songs/index.html')

def songs(request):
    """Songs page"""
    songs = Song.objects.order_by()
    context = {'songs':songs}
    return render(request, 'songs/songs.html', context)

def song(request, song_id):
    """Page for an individual song"""
    songs = Song.objects.get(id=song_id)
    
    english_title = songs.english_title
    arabic_title = songs.arabic_title
    german_title = songs.german_title
    english_text = songs.english_text
    arabic_text = songs.arabic_text
    german_text = songs.german_text

    context = {'songs':songs, 'english_title':english_title, 'arabic_title':arabic_title, 'german_title':german_title, 'english_text':english_text, 'arabic_text':arabic_text, 'german_text':german_text}
    return render(request, 'songs/song.html', context)
