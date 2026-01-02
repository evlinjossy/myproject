from django.urls import path
from features.authors.apps import AuthorsConfig
from features.authors.controller import AuthorViewController
# from .controller import create, get_all , get, update, delete

app_name = AuthorsConfig.name
urlpatterns = [
    path('create/', AuthorViewController.create, name='author-create'),
    path('get_all/', AuthorViewController.get_all, name='author-get-all'),
    path('get/', AuthorViewController.get, name='author-get'),
    path('update/', AuthorViewController.update, name='author-update'),
    path('delete/', AuthorViewController.delete, name='author-delete'),
]
