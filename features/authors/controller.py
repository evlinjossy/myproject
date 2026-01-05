from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from features.authors.serializers.request.create import CreateAuthorSerializer
from features.authors.serializers.request.update import UpdateAuthorSerializer
from features.authors.serializers.request.get_all import GetAllAuthorSerializer
from features.authors.serializers.request.delete import DeleteAuthorRequestSerializer

from features.authors.views import AuthorView
from features.common.serializer_validations import SerializerValidations
from features.authors.serializers.request.get import AuthorGetSerializer


class AuthorViewController:
    sort_by = {"name": "name"}

    @api_view(["POST"])
    @SerializerValidations(
        serializer=CreateAuthorSerializer,
        exec_func="AuthorView().create_extract(request)",
    ).validate
    def create(request: Request) -> Response:
        return AuthorView().create_extract(
            params=request.params,  
            # token_payload=request.payload
        )

    @api_view(["GET"])
    @SerializerValidations(serializer=GetAllAuthorSerializer).validate
    def get_all(request: Request) -> Response:
        return AuthorView().get_all_extract(
            params=request.params,  
            # token_payload=request.payload,
        )

    @api_view(["GET"])
    @SerializerValidations(serializer=AuthorGetSerializer).validate
    def get(request: Request) -> Response:
        return AuthorView().get_extract(
            params=request.params,  
            # token_payload=request.payload
        )

    @api_view(["PUT"])
    @SerializerValidations(
        serializer=UpdateAuthorSerializer,
        exec_func="AuthorView().update_extract(request)",
    ).validate
    def update(request: Request) -> Response:
        return AuthorView().update_extract(
            params=request.params,  
            # token_payload=request.payload,
        )

    @api_view(["DELETE"])
    @SerializerValidations(
        serializer=DeleteAuthorRequestSerializer,
        exec_func="AuthorView().delete_extract(request)",
    ).validate
    def delete(request: Request) -> Response:
        return AuthorView().delete_extract(
            params=request.params,  
            # token_payload=request.payload,
        )
