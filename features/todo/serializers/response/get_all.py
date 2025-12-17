from rest_framework import serializers
from .todo_item import TodoItemSerializer

class GetAllResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    data = TodoItemSerializer(many=True)
