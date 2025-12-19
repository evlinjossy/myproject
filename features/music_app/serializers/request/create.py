from rest_framework import serializers
from features.music_app.dataclasses.request.create import CreateMusicData

class CreateMusicSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    artist = serializers.CharField(max_length=255)
    album = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    release_date = serializers.DateField(required=False, allow_null=True)

    def create(self, validated_data) -> CreateMusicData:
        return CreateMusicData(**validated_data)
