from rest_framework import serializers
from features.common.serializers.response.api_response import ApiResponseSerializer

class AuthorGetAllItemSerializer(serializers.Serializer):
    author_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    language = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)

class AuthorGetAllDataSerializer(serializers.Serializer):
    items = AuthorGetAllItemSerializer(many=True)
    page = serializers.IntegerField()
    total_page = serializers.IntegerField()
    total_count = serializers.IntegerField()
    next_page_required = serializers.BooleanField()


class AuthorGetAllResponseSerializer(ApiResponseSerializer):
    data = AuthorGetAllDataSerializer(required=False)