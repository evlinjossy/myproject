from django.db import models
from django.utils import timezone

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "authors"

    @classmethod
    def create_author(cls, name: str, age: int, language: str, country: str) -> int:
        author = cls(
            name=name,
            age=age,
            language=language,
            country=country,
            created_at=timezone.now()
        )
        author.save()
        return author.author_id

    def __str__(self):
        return self.name
