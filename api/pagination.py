from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10                     # default if client doesn't provide ?limit
    page_size_query_param = 'limit'    # client can control size with ?limit=
    max_page_size = 100                # safety cap


