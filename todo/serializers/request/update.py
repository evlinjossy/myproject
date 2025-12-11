from rest_framework import serializers

class UpdateTodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(max_length=500, required=False)
    is_completed = serializers.BooleanField(required=False)
    due_date = serializers.DateField(required=False)
