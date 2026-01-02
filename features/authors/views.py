from django.core.paginator import Paginator, EmptyPage
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from features.authors.models import Author
from features.common.Utils import Utils


class AuthorView:
    def __init__(self):
        self.data_created = "Author created successfully"
        self.data_updated = "Author updated successfully"
        self.data_deleted = "Author deleted successfully"
        self.data_fetched = "Data fetched successfully"
        self.data_not_found = "Author not found"

   
    def create_extract(self, params, token_payload=None) -> Response:
        with transaction.atomic():
            Author.create_author(
                name=params.name,
                age=params.age,
                language=params.language,
                country=params.country,
            )

        return Response(
            status=status.HTTP_201_CREATED,
            data=Utils.success_response_data(message=self.data_created),
        )

    # -------------------------
    # GET ALL AUTHORS WITH PAGINATION
    # -------------------------
    def get_all_extract(self, params, token_payload=None) -> Response:
        queryset = Author.objects.all() 
        page_size = int(params.get('page_size', 10))  # default 10 if not provided
        paginator = Paginator(queryset, page_size)

        page_num = int(params.get('page', 1))  # get page number safely

        try:
            page = paginator.page(page_num)
        except EmptyPage:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=Utils.error_response_data("Page number exceeded"),
            )

        # Convert page to list of dicts
        data = [
            {
                "author_id": obj.author_id,
                "name": obj.name,
                "age": obj.age,
                "language": obj.language,
                "country": obj.country,
            }
            for obj in page
        ]

        data = Utils.add_page_parameter(
            final_data=data,
            page_num=page_num,
            total_page=paginator.num_pages,
            total_count=paginator.count,
            next_page_required=page_num < paginator.num_pages,
        )

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message=self.data_fetched,
                data=data,
            ),
        )
    # Convert page to list of dicts
 

    # -------------------------
    # GET SINGLE AUTHOR
    # -------------------------
    def get_extract(self, params, token_payload=None) -> Response:
        author_id=params.get('author_id')

        if not author_id:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=Utils.error_response_data("author_id is required"),
            )
        try:
            author = Author.objects.get(author_id=author_id, is_active=True)
        except Author.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=Utils.error_response_data(self.data_not_found),
            )

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message=self.data_fetched,
                data={
                    "author_id": author.author_id,
                    "name": author.name,
                    "age": author.age,
                    "language": author.language,
                    "country": author.country,
                },
            ),
        )

    # -------------------------
    # UPDATE AUTHOR
    # -------------------------
    def update_extract(self, params, token_payload=None) -> Response:
        try:
            author = Author.objects.get(author_id=params.author_id, is_active=True)
        except Author.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=Utils.error_response_data(self.data_not_found),
            )

        # Only update fields if provided
        for field in ["name", "age", "language", "country"]:
            if getattr(params, field, None) is not None:
                setattr(author, field, getattr(params, field))

        author.save()

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(message=self.data_updated),
        )

    # -------------------------
    # DELETE AUTHOR (SOFT)
    # -------------------------
    def delete_extract(self, params, token_payload=None) -> Response:
        try:
            author = Author.objects.get(author_id=params.author_id, is_active=True)
        except Author.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=Utils.error_response_data(self.data_not_found),
            )

        # Soft delete
        author.is_active = False
        author.save()

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(message=self.data_deleted),
        )
