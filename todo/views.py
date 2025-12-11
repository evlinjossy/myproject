from rest_framework.response import Response
from .models import Todo
from .dataclasses.request.create import CreateTodoData
from .dataclasses.request.update import UpdateTodoData

class TodoView:
    data_created = "Todo created successfully"
    data_updated = "Todo updated successfully"
    data_deleted = "Todo deleted successfully"

    def create_todo(self, params):
        todo_data = CreateTodoData(**params)
        todo = Todo.create_todo({
            "title": todo_data.title,
            "description": todo_data.description,
            "due_date": todo_data.due_date,
            "is_completed": todo_data.is_completed
        })
        response = {
            "message": self.data_created,
            "data": {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "is_completed": todo.is_completed,
                "due_date": todo.due_date,
                "created_at": todo.created_at,
                "updated_at": todo.updated_at
            }
        }
        return Response(response)

    def update_todo(self, todo_id, params):
        todo = Todo.objects.filter(id=todo_id).first()
        if not todo:
            return Response({"message": "Todo not found"}, status=404)

        todo_data = UpdateTodoData(**params)
        todo.update_todo({
            "title": todo_data.title,
            "description": todo_data.description,
            "due_date": todo_data.due_date,
            "is_completed": todo_data.is_completed
        })
        response = {
            "message": self.data_updated,
            "data": {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "is_completed": todo.is_completed,
                "due_date": todo.due_date,
                "created_at": todo.created_at,
                "updated_at": todo.updated_at
            }
        }
        return Response(response)

    def get_todo(self, todo_id=None):
        if todo_id:
            data = [Todo.objects.filter(id=todo_id).first()]
        else:
            data = Todo.objects.all()

        response = {
            "message": "Todos fetched successfully",
            "data": [
                {
                    "id": t.id,
                    "title": t.title,
                    "description": t.description,
                    "is_completed": t.is_completed,
                    "due_date": t.due_date,
                    "created_at": t.created_at,
                    "updated_at": t.updated_at
                } for t in data if t
            ]
        }
        return Response(response)

    def delete_todo(self, todo_id):
        todo = Todo.objects.filter(id=todo_id).first()
        if not todo:
            return Response({"message": "Todo not found"}, status=404)
        todo.delete()
        return Response({"message": self.data_deleted})
