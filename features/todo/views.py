from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .dataclasses.request.create import CreateTodoData
from .dataclasses.request.update import UpdateTodoData
from features.common.Utils import Utils  # only import Utils

class TodoView:
    data_created = "Todo created successfully"
    data_updated = "Todo updated successfully"
    data_deleted = "Todo deleted successfully"

    def create_todo(self, params):
        todo_data = CreateTodoData(**params)
        todo = Todo.objects.create(
            title=todo_data.title,
            description=todo_data.description,
            due_date=todo_data.due_date,
            is_completed=todo_data.is_completed
        )

        data = {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "is_completed": todo.is_completed,
            "due_date": todo.due_date,
            "created_at": todo.created_at,
            "updated_at": todo.updated_at
        }

        return Response(
            status=status.HTTP_201_CREATED,
            data=Utils.success_response_data(message=self.data_created, data=data)
        )

    def update_todo(self, todo_id, params):
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return Response(
                {"message": f"Todo with id {todo_id} not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        for key, value in params.items():
            setattr(todo, key, value)
        todo.save()

        data = {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "is_completed": todo.is_completed,
            "due_date": todo.due_date,
            "created_at": todo.created_at,
            "updated_at": todo.updated_at
        }

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(message=self.data_updated, data=data)
        )

    def get_todo(self, todo_id=None):
        if todo_id:
            todos = [Todo.objects.filter(id=todo_id).first()]
        else:
            todos = Todo.objects.all()

        data = [
            {
                "id": t.id,
                "title": t.title,
                "description": t.description,
                "is_completed": t.is_completed,
                "due_date": t.due_date,
                "created_at": t.created_at,
                "updated_at": t.updated_at
            }
            for t in todos if t
        ]

        return Response(
            data=Utils.success_response_data(message="Todos fetched successfully", data=data)
        )

    def delete_todo(self, todo_id):
        todo = Todo.objects.filter(id=todo_id).first()
        if not todo:
            return Response(
                Utils.error_response_data("Todo not found"),
                status=status.HTTP_404_NOT_FOUND
            )
        todo.delete()
        return Response(
            data=Utils.success_response_data(message=self.data_deleted)
        )
