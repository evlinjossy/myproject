from django.db import models
from django.utils import timezone
from django.db.models import Q, F
from features.common.constants import StaticAuthor  # or correct path


from features.authors.dataclass.request.get import GetAuthorRequest
from features.authors.dataclass.request.get_all import GetAllAuthorsRequest

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

    
    def create_author(self, name: str, age: int, language: str, country: str) :
        self.name = name
        self.age = age
        self.language = language
        self.country = country
        self.is_active = True
        self.created_at = timezone.now()
        self.save()
        return self.author_id
    
    @staticmethod
    def update_author(
        author_id: int, name: str, age: int, language: str, country: str,
    ):
        authorr=Author.objects.filter(
            author_id=author_id, is_active=True
        ).first()
        if not authorr:
            raise ValueError(
                f"Author with id '{author_id}' does not exist."
            )
        if name:
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Name must be a string.")
            authorr.name = name
        if age:
            if not isinstance(age, int) or age <= 0:
                raise ValueError("Age must be a positive integer.")
            authorr.age = age
        if language:
            authorr.language = language
        if country:
            authorr.country = country

        authorr.save()

    @staticmethod
    def delete_author(author_id: int):
            author_del=Author.objects.filter(
                author_id=author_id, is_active=True
            )
            found_author=list(author_del.values_list('author_id',flat=True))
            missing_author=set([author_id])-set(found_author)
            if missing_author:
                raise ValueError(
                    f"Author with id '{missing_author.pop()}' does not exist."
                )
            author_del.delete()
            return True
        
    @staticmethod
    def getAuthor(params:GetAuthorRequest, author_id: int):
        filters=Q(author_id=author_id,is_active=True)
        
        if params.name:
            filters &=Q(name=params.name)
        if params.age:
            filters &=Q(age=params.age)
        if params.language:
            filters &=Q(language=params.language)
        if params.country:
            filters &= Q(country=params.country)
            
        author_query = Author.objects.filter(filters).values(
            "author_id", "name", "age", "language", "country"
        ).first()

        return author_query
    
    @staticmethod
    def get_all_author(params:GetAllAuthorsRequest):
        filters=Q(is_active=True)
        filter_vlaue={
            StaticAuthor.name:F("name"),
            StaticAuthor.age:F("age"),
            StaticAuthor.language:F("language"),
            StaticAuthor.country:F("country"),
        }
        query=Author.objects.filter(filters)
        return query.values("author_id", "name", "age", "language", "country")


        