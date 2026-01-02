from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction
from features.authors.models.authors import Author
from django.core.paginator import EmptyPage
from features.music_app.models.music import Music
from features.common.Utils import Utils


class MusicView:
    def __init__(self):
            self.data_created = "Music created successfully"
            self.data_updated = "Music updated successfully"
            self.data_deleted = "Music deleted successfully"
            self.data_fetched = "Data fetched successfully"
            self.data_not_found = "Music not found"

    def create_music(self, params, token_payload=None) -> Response:
            author_id = params.get('author_id')
            if not author_id:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data=Utils.error_response_data("author_id is required"),
                )
            author = Author.objects.get(pk=author_id)
            music_id = Music.create_music(
                title=params.get('title'),
                author=author,
                album=params.get('album'),
                release_date=params.get('release_date')
)

            data = {"music_id": music_id}


            return Response(
                status=status.HTTP_201_CREATED,
                data=Utils.success_response_data(message=self.data_created,)
            )


    def list_music(self, params, token_payload=None) -> Response:
            queryset = Music.objects.all().order_by('-created_at')
            page_size=int(params.get('page_size',10))
            page_num=int(params.get('page',1))  

            paginator=Paginator(queryset,page_size)


            try:
                page=paginator.page(page_num)
            except EmptyPage:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data=Utils.error_response_data("Page number exceeded"),
                )

            data = [
                {
                    "music_id": obj.music_id,
                    "title": obj.title,
                    "author_id": obj.author.author_id,
                    "author_name": obj.author.name,
                    "album": obj.album,
                    "release_date": obj.release_date,
                }
                for obj in page
            ]

            data = Utils.add_page_parameter(
                final_data=data,
                page_num=page_num,
                total_page=paginator.num_pages,
                total_count=paginator.count,
                next_page_required=paginator.num_pages != page_num,
            )

            return Response(
                status=status.HTTP_200_OK,
                data=Utils.success_response_data(
                    message=self.data_fetched,
                    data=data
                )
            )

        
    def retrieve_music(self, params, music_id: int, token_payload=None) -> Response:
            # music_id= params.get('music_id')

            # if not music_id:
            #     return Response(
            #         status=status.HTTP_400_BAD_REQUEST,
            #         data=Utils.error_response_data("music_id is required"),
            #     )
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
                "author_id":music.author.author_id,
                "author_name": music.author.name,
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
            author_id = params.get('author_id')
            if not author_id:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data=Utils.error_response_data("author_id is required"),
                )

            author = Author.objects.get(pk=author_id)
            music.author = author
            music.title = params.get('title')
            music.album = params.get('album')
            music.release_date = params.get('release_date')
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
