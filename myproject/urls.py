from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todo/', include('features.todo.urls')),        # Todo endpoints
    path('api/music/', include('features.music_app.urls')), # Music endpoints
    path('api/authors/', include('features.authors.urls')), # Authors endpoints
]
