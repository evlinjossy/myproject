from rest_framework import serializers
from features.music_app.dataclasses.request.update import UpdateMusicData

class UpdateMusicSerializer(serializers.Serializer):
    music_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255, required=False)
    author_name = serializers.CharField(max_length=255, required=False)
    album = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    release_date = serializers.DateField(required=False, allow_null=True)

    def create(self, validated_data) -> UpdateMusicData:
        return UpdateMusicData(**validated_data)
