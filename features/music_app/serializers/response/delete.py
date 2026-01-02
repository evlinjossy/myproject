from rest_framework import serializers
from features.common.serializers.response.api_response import ApiResponseSerializer

class MusicDeleteDataSerializer(serializers.Serializer):
    music_id = serializers.IntegerField()
    message = serializers.CharField(max_length=255, default="Music deleted successfully")

class MusicDeleteResponseSerializer(ApiResponseSerializer):
    data = MusicDeleteDataSerializer(required=False)
