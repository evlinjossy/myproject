from django.urls import path
from .apps import TodoConfig
from .controller import TodoController

app_name = TodoConfig.name  # Use app_name for namespacing

urlpatterns = [
    path('create/', TodoController.create_item, name='todo_create'),
    path('get_all/', TodoController.get_item, name='todo_get_all'),
    path('get/<int:todo_id>/', TodoController.get_item, name='todo_get'),
    path('update/<int:todo_id>/', TodoController.update_item, name='todo_update'),
    path('delete/<int:todo_id>/', TodoController.delete_item, name='todo_delete'),
]
