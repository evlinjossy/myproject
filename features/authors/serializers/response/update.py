from rest_framework import serializers
from features.common.serializers.response.api_response import ApiResponseSerializer

class AuthorUpdateDataSerializer(serializers.Serializer):
    author_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    language = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)

class AuthorUpdateResponseSerializer(ApiResponseSerializer):
    data = AuthorUpdateDataSerializer(required=False)