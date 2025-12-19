from rest_framework import serializers
from features.music_app.dataclasses.request.get_all import GetAllMusicData

class GetAllMusicSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=1, min_value=1)
    page_size = serializers.IntegerField(required=False, default=10, min_value=1, max_value=100)
    search = serializers.CharField(required=False, allow_blank=True)
    sort_by = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data) -> GetAllMusicData:
        return GetAllMusicData(**validated_data)
