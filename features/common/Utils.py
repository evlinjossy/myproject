import random
import urllib


class Utils:

    @staticmethod
    def success_response_data(message, data=None):
        response = {
            "status": True,
            "message": message
        }
        if data is not None:
            response["data"] = data
        return response

    @staticmethod
    def error_response_data(message, errors=None):
        response = {
            "status": False,
            "message": message
        }
        if errors:
            response["errors"] = errors
        return response




def todo_data_response(todo):
    return {
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "is_completed": todo.is_completed,
        "due_date": todo.due_date,
        "created_at": todo.created_at,
        "updated_at": todo.updated_at,
    }
