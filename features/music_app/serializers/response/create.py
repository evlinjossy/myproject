from rest_framework import serializers
from features.common.serializers.response.api_response import ApiResponseSerializer

class MusicCreateDataSerializer(serializers.Serializer):
    music_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    author_id = serializers.IntegerField()
    author_name = serializers.CharField(max_length=255)
    album = serializers.CharField(max_length=255, allow_null=True, required=False)
    release_date = serializers.DateField(allow_null=True, required=False)

class MusicCreateResponseSerializer(ApiResponseSerializer):
    data = MusicCreateDataSerializer(required=False)
