# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Song(models.Model):
   
    english_title = models.CharField(max_length=200)
    arabic_title = models.CharField(max_length=200)
    german_title = models.CharField(max_length=200)

    english_text = models.TextField()
    arabic_text = models.TextField()
    german_text = models.TextField()

    def __str__(self):
        return self.english_title
