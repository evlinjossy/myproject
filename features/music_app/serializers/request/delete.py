from rest_framework import serializers
from features.music_app.dataclasses.request.delete import DeleteMusicData

class DeleteMusicSerializer(serializers.Serializer):
    music_id = serializers.IntegerField()

    def create(self, validated_data) -> DeleteMusicData:
        return DeleteMusicData(**validated_data)
