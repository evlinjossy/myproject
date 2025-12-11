from rest_framework import serializers
from .todo_item import TodoItemSerializer

class CreateResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    data = TodoItemSerializer()
