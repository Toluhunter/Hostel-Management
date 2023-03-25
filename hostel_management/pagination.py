from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):

    page_size = 10
    page_size_query_param = "s"
    page_query_param = "q"
    max_page_size = 25
