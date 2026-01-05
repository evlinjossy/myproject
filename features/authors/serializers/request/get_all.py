from rest_framework import serializers
from features.authors.dataclass.request.get_all import GetAllAuthorsRequest

class GetAllAuthorSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(required=False, default=1, min_value=1)
    limit = serializers.IntegerField(required=False, default=10, min_value=1, max_value=100)
    search = serializers.CharField(required=False, allow_blank=True)
    sort_by = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data) -> GetAllAuthorsRequest:
        validated_data["search"] = validated_data.get("search") or None
        validated_data["sort_by"] = validated_data.get("sort_by") or None
        return GetAllAuthorsRequest(**validated_data)