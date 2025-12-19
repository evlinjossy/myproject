class Utils:

    # ✅ EXISTING – DO NOT TOUCH
    @staticmethod
    def success_response_data(message: str, data=None):
        return {
            "status": True,
            "message": message,
            "data": data
        }

    @staticmethod
    def error_response_data(message: str, errors=None):
        return {
            "status": False,
            "message": message,
            "errors": errors
        }

    # ✅ NEW – FOR PAGINATION (Music / Future apps)
    @staticmethod
    def add_page_parameter(
        final_data,
        page_num: int,
        total_page: int,
        total_count: int,
        next_page_required: bool = False
    ):
        response = {
            "data": final_data,
            "presentPage": page_num,
            "totalPage": total_page,
            "totalCount": total_count
        }

        if next_page_required:
            response["hasNext"] = True
            response["nextPage"] = page_num + 1
        else:
            response["hasNext"] = False

        return response
