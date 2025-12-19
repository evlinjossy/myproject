from rest_framework import serializers
from features.music_app.dataclasses.request.get import GetMusicData

class GetMusicSerializer(serializers.Serializer):
    music_id = serializers.IntegerField()

    def create(self, validated_data) -> GetMusicData:
        return GetMusicData(**validated_data)
