from django.db import models
from django.utils import timezone


class Music(models.Model):
    music_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)

    album = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    release_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.title} - {self.artist}"
