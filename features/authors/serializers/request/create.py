from rest_framework import serializers
from features.authors.dataclass.request.create import AuthorRequest

class CreateAuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    language = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)

    def create(self, validated_data) -> AuthorRequest:
        return AuthorRequest(**validated_data)
