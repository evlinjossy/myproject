from rest_framework import serializers

class CreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    due_date = serializers.DateField(required=False)
    is_completed = serializers.BooleanField(required=False)
