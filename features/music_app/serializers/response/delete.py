from rest_framework import serializers
from features.common.serializers.response.api_response import APiResponseSerializer

class MusicDeleteDataSerializer(serializers.Serializer):
    music_id = serializers.IntegerField()
    message = serializers.CharField(max_length=255, default="Music deleted successfully")

class MusicDeleteResponseSerializer(APiResponseSerializer):
    data = MusicDeleteDataSerializer(required=False)
