from rest_framework import serializers

class DeleteResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
