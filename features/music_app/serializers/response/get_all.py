from rest_framework import serializers
from features.common.serializers.response.api_response import APiResponseSerializer

class MusicGetAllItemSerializer(serializers.Serializer):
    music_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    artist = serializers.CharField(max_length=255)
    album = serializers.CharField(max_length=255, allow_null=True, required=False)
    release_date = serializers.DateField(allow_null=True, required=False)

class MusicGetAllDataSerializer(serializers.Serializer):
    items = MusicGetAllItemSerializer(many=True)
    total = serializers.IntegerField()

class MusicGetAllResponseSerializer(APiResponseSerializer):
    data = MusicGetAllDataSerializer(required=False)
