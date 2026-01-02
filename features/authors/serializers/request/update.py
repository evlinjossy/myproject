from rest_framework import serializers
from features.authors.dataclass.request.update import AuthorUpdateRequest

class UpdateAuthorSerializer(serializers.Serializer):
    author_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255, required=False)
    age = serializers.IntegerField(required=False)
    language = serializers.CharField(max_length=100, required=False)
    country = serializers.CharField(max_length=100, required=False)

    def to_dataclass(self, validated_data) -> AuthorUpdateRequest:
        return AuthorUpdateRequest(**validated_data)
