from rest_framework import serializers
from features.common.serializers.response.api_response import ApiResponseSerializer

class AuthorCreateDataSerializer(serializers.Serializer):
    author_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    language = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)


class AuthorCreateResponseSerializer(ApiResponseSerializer):
    data = AuthorCreateDataSerializer(required=False)