from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter
from rest_framework import serializers

from features.authors.dataclass.request.get import GetAuthorRequest


class AuthorGetSerializer(serializers.Serializer):
    author_id = serializers.IntegerField(required=True)

    def to_dataclass(self, validated_data) -> GetAuthorRequest:
        return GetAuthorRequest(**validated_data)

    @staticmethod
    def get_parameters():
        return [
            OpenApiParameter(
                name="author_id",
                description="ID of the author",
                required=True,
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            )
        ]
