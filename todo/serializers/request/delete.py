from rest_framework import serializers

class DeleteTodoSerializer(serializers.Serializer):
    todo_id = serializers.IntegerField()
