from django.db import models
from django.utils import timezone
from typing import Optional
from datetime import date
from features.authors.models.authors import Author  

class Music(models.Model):
    music_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='musics')
    album = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "music"

    @classmethod
    def create_music(
        cls,
        title: str,
        author: Author,
        album: Optional[str] = None,
        release_date: Optional[date] = None
    ):
        music = cls.objects.create(
            title=title,
            author=author,
            album=album,
            release_date=release_date
        )
        return music.music_id


        
