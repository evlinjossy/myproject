from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response

from features.music_app.models.music import Music
from features.common.utils import Utils


class MusicView:
    def __init__(self):
        self.data_created = "Music created successfully"
        self.data_updated = "Music updated successfully"
        self.data_deleted = "Music deleted successfully"
        self.data_fetched = "Data fetched successfully"
        self.data_not_found = "Music not found"

    def create_music(self, params, token_payload=None) -> Response:
        music = Music.objects.create(
            title=params.title,
            artist=params.artist,
            album=params.album,
            release_date=params.release_date
        )

        return Response(
            status=status.HTTP_201_CREATED,
            data=Utils.success_response_data(
                message=self.data_created,
                data={"music_id": music.music_id}
            )
        )


    def list_music(self, params, token_payload=None) -> Response:
        queryset = Music.objects.all().order_by("-created_at")

        if params.search:
            queryset = queryset.filter(title__icontains=params.search)

        paginator = Paginator(queryset, params.page_size)

        if paginator.num_pages < params.page:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=Utils.error_response_data("Page number exceeded")
            )

        page = paginator.page(params.page)

        data = [
            {
                "music_id": obj.music_id,
                "title": obj.title,
                "artist": obj.artist,
                "album": obj.album,
                "release_date": obj.release_date,
            }
            for obj in page
        ]

        data = Utils.add_page_parameter(
            final_data=data,
            page_num=params.page,
            total_page=paginator.num_pages,
            total_count=paginator.count,
            next_page_required=paginator.num_pages != params.page,
        )

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message=self.data_fetched,
                data=data
            )
        )

    
    def retrieve_music(self, params, music_id: int, token_payload=None) -> Response:
        try:
            music = Music.objects.get(pk=music_id)
        except Music.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=Utils.error_response_data(self.data_not_found)
            )

        data = {
            "music_id": music.music_id,
            "title": music.title,
            "artist": music.artist,
            "album": music.album,
            "release_date": music.release_date,
        }

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message=self.data_fetched,
                data=data
            )
        )

    
    def update_music(self, params, music_id: int, token_payload=None) -> Response:
        try:
            music = Music.objects.get(pk=music_id)
        except Music.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=Utils.error_response_data(self.data_not_found)
            )

        music.title = params.title
        music.artist = params.artist
        music.album = params.album
        music.release_date = params.release_date
        music.save()

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message=self.data_updated
            )
        )

    
    def delete_music(self, params, music_id: int, token_payload=None) -> Response:
        try:
            music = Music.objects.get(pk=music_id)
        except Music.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=Utils.error_response_data(self.data_not_found)
            )

        music.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message=self.data_deleted
            )
        )
