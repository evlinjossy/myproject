from rest_framework import serializers

class GetTodoSerializer(serializers.Serializer):
    todo_id = serializers.IntegerField(required=False)  # optional for "get all"
