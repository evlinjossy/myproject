from rest_framework import serializers
from features.common.serializers.response.api_response import ApiResponseSerializer

class AuthorDeleteDataSerializer(serializers.Serializer):
    author_id = serializers.IntegerField()
    message = serializers.CharField(max_length=255, default="Author deleted successfully")

class AuthorDeleteResponseSerializer(ApiResponseSerializer):
    data = AuthorDeleteDataSerializer(required=False)