from drf_spectacular.utils import extend_schema
from features.todo.serializers import request
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .dataclasses.request.create import CreateTodoData
from .dataclasses.request.update import UpdateTodoData
from .dataclasses.request.get import GetTodoData
from .dataclasses.request.delete import DeleteTodoData

from .serializers.request.create import CreateRequestSerializer
from .serializers.request.update import UpdateTodoSerializer
from .views import TodoView



class TodoController:
    sort_by = {}

    @extend_schema(
        description="Create a Todo item",
        request=CreateRequestSerializer,

    )
    @api_view(['POST'])
    def create_item(request: Request) -> Response: 
        todo_data = CreateTodoData(**request.data) 
        return TodoView().create_todo(params=todo_data.__dict__)

    @extend_schema(
        description="Get a single Todo or all Todos",
        
    )
    @api_view(['GET'])
    def get_item(request: Request, todo_id: int = None) -> Response:
        todo_data = GetTodoData(todo_id=todo_id)
        return TodoView().get_todo(todo_id=todo_data.todo_id)

    @extend_schema(
        description="Update a Todo item",
        request=UpdateTodoSerializer,
       
    )
    @api_view(['PUT'])
    def update_item(request, todo_id):
        todo_data = UpdateTodoData(**request.data)
        return TodoView().update_todo(todo_id=todo_id, params=todo_data.__dict__)


    @extend_schema(
        description="Delete a Todo item",
        
    )
    @api_view(['DELETE'])
    def delete_item(request: Request, todo_id: int) -> Response:
        todo_data = DeleteTodoData(todo_id=todo_id)
        return TodoView().delete_todo(todo_id=todo_data.todo_id)