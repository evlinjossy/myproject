from rest_framework import serializers
from features.authors.dataclass.request.delete import AuthorDeleteRequest

class DeleteAuthorRequestSerializer(serializers.Serializer):
    author_id=serializers.IntegerField()

    def create(self,validated_data)->AuthorDeleteRequest:
        return AuthorDeleteRequest(**validated_data)