from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from features.music_app.serializers.request.create import CreateMusicSerializer
from features.music_app.serializers.request.update import UpdateMusicSerializer
from features.music_app.serializers.request.get_all import GetAllMusicSerializer
from features.music_app.serializers.response.create import MusicCreateResponseSerializer
from features.music_app.serializers.response.update import MusicUpdateResponseSerializer
from features.music_app.serializers.response.delete import MusicDeleteResponseSerializer
from features.music_app.serializers.response.get import MusicGetResponseSerializer
from features.music_app.serializers.response.get_all import MusicGetAllResponseSerializer
from features.music_app.views import MusicView
from features.common.serializer_validations import SerializerValidations



class MusicViewController:

    @extend_schema(
        description="Add a music record",
        request=CreateMusicSerializer,
        responses=MusicCreateResponseSerializer
    )
    @api_view(['POST'])
    @SerializerValidations(serializer=CreateMusicSerializer).validate
    def create(request: Request) -> Response:
        params=request.data
        token_payload=getattr(request,'payload',None)
        return MusicView().create_music(params=request.data)

    @extend_schema(
        description="Get all music records",
        # parameters=GetAllMusicSerializer.get_all_parameters(),
        responses=MusicGetAllResponseSerializer
    )
    @api_view(['GET'])
    @SerializerValidations(serializer=GetAllMusicSerializer).validate
    def get_all(request: Request) -> Response:
        return MusicView().list_music(params=request.query_params, token_payload=getattr(request,'payload',None))

    @extend_schema(
        description="Get a single music record",
        responses=MusicGetResponseSerializer
    )
    @api_view(['GET'])
    @SerializerValidations(serializer=None).validate
    def get(request: Request) -> Response:
        music_id = request.query_params.get('music_id')
        if not music_id:
            return Response({"error":"music id is required"}, status=400)
        return MusicView().retrieve_music(params=request.params, music_id=int(music_id),
                                          token_payload=getattr(request,'payload',None))

    @extend_schema(
        description="Update a music record",
        request=UpdateMusicSerializer,
        responses=MusicUpdateResponseSerializer
    )
    @api_view(['PUT'])
    @SerializerValidations(serializer=UpdateMusicSerializer).validate
    def update(request: Request) -> Response:
        music_id=request.data.get('music_id')
        if not music_id:
            return Response({"error":"music id is required"}, status=400)
        return MusicView().update_music(params=request.data, music_id=int(music_id),
                                        token_payload=getattr(request,'payload',None))

    @extend_schema(
        description="Delete a music record",
        responses=MusicDeleteResponseSerializer
    )
    @api_view(['DELETE'])
    @SerializerValidations(serializer=None).validate
    def delete(request: Request) -> Response:
        music_id = request.data.get('music_id')
        if not music_id:
            return Response({"error":"music id is required"}, status=400)
        return MusicView().delete_music(params=request.data, music_id=music_id,
                                        token_payload=getattr(request,'payload',None))