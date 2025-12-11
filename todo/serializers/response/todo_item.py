from rest_framework import serializers

class TodoItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    is_completed = serializers.BooleanField()
    due_date = serializers.DateField(required=False)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
