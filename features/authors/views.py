from django.core.paginator import Paginator, EmptyPage
from django.db import transaction
from features.authors.dataclass.request.delete import AuthorDeleteRequest
from features.authors.dataclass.request.get import GetAuthorRequest
from features.authors.dataclass.request.get_all import GetAllAuthorsRequest
from features.authors.dataclass.request.update import AuthorUpdateRequest
from rest_framework import status
from rest_framework.response import Response
from features.authors.dataclass.request.create import AuthorRequest

from features.authors.models import Author
from features.common.Utils import Utils


class AuthorView:
    def __init__(self):
        self.data_created = "Author created successfully"
        self.data_updated = "Author updated successfully"
        self.data_deleted = "Author deleted successfully"
        self.data_fetched = "Data fetched successfully"
        self.data_not_found = "Author not found"


    def create_extract(self, params:AuthorRequest, token_payload=None):
        with transaction.atomic():
            Author().create_author(
                name=params.name,
                age=params.age,
                language=params.language,
                country=params.country,
            )

        return Response(
            status=status.HTTP_201_CREATED,
            data=Utils.success_response_data(message=self.data_created),
        )

    def get_all_extract(self, params:GetAllAuthorsRequest, token_payload=None):
        pages=Paginator(Author.get_all_author(params=params),params.limit)

        if pages.num_pages< params.page_num:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=Utils.error_response_data("Page number exceeded"),
            )
        page_data=pages.page(params.page_num)
        get_all_data=Utils.add_page_parameter(final_data=page_data.object_list,page_num=params.page_num,
                                              total_page=pages.num_pages,total_count=pages.count,
                                              next_page_required=True if pages.num_pages!=params.page_num
                                              else False)
        
        return Response(status=status.HTTP_200_OK,
                        data=Utils.success_response_data(message=self.data_fetched,data=get_all_data),)


    def get_extract(self, params:GetAuthorRequest, token_payload=None) :
        response_data=Author.getAuthor(params=params,author_id=params.author_id)
        return Response(status=status.HTTP_200_OK,data=Utils.success_response_data(message=self.data_fetched, data=response_data))

    # -------------------------
    # UPDATE AUTHOR
    # -------------------------
    def update_extract(self, params:AuthorUpdateRequest, token_payload=None) :
        with transaction.atomic():
            Author().update_author(
                author_id=params.author_id,
                name=params.name,
                age=params.age,
                language=params.language,
                country=params.country,
            )
            return Response(status=status.HTTP_200_OK,
                            data=Utils.success_response_data(message=self.data_updated),)
        
    # -------------------------
    # DELETE AUTHOR 
    # -------------------------
    def delete_extract(self, params:AuthorDeleteRequest, token_payload=None) :
        with transaction.atomic():
            Author().delete_author(
                author_id=params.author_id,
            )

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(message=self.data_deleted),
        )
