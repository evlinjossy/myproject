class PaginationUtils:
    @staticmethod
    def add_page_parameter(final_data, page_num, total_page, total_count, present_url, next_page_required=False):
        to_return = {
            "data": final_data,
            "presentPage": page_num,
            "totalPage": total_page,
            "totalCount": total_count
        }
        if next_page_required and total_page > 1:
            from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
            parsed_url = urlparse(present_url)
            query_params = dict(parse_qsl(parsed_url.query))
            query_params['page_num'] = str(page_num + 1)
            new_query = urlencode(query_params)
            next_page_url = urlunparse((
                parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query, parsed_url.fragment
            ))
            to_return['nextPageUrl'] = next_page_url
        return to_return
