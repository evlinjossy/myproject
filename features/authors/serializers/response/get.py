from rest_framework import serializers
from features.common.serializers.response.api_response import ApiResponseSerializer

class AuthorGetDataSerializer(serializers.Serializer):
    author_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    language = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)

class AuthorGetResponseSerializer(ApiResponseSerializer):
    data = AuthorGetDataSerializer(required=False)