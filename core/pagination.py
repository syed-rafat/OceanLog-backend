from rest_framework.pagination import PageNumberPagination


class HomePagination(PageNumberPagination):
    page_size = 8
    
    # can have different page size on request basis using this
    # page_size_query_param = 'page_size'
    # max_page_size = 10000