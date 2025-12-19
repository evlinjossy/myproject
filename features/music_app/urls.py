from django.urls import path
from .apps import MusicAppConfig
from .controller import MusicViewController

app_name = MusicAppConfig.name  # namespacing

urlpatterns = [
    path('create/', MusicViewController.create, name='music_create'),
    path('get_all/', MusicViewController.get_all, name='music_get_all'),
    path('get/', MusicViewController.get, name='music_get'),
    path('update/', MusicViewController.update, name='music_update'),
    path('delete/', MusicViewController.delete, name='music_delete'),
]
