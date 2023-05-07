from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Author, Book
from .my_permissions import IsAdminOrAuthOnly
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import permissions


class BookApiListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrAuthOnly]
    pagination_class = BookApiListPagination
    # authentication_classes = [TokenAuthentication]


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrAuthOnly]
    # authentication_classes = [TokenAuthentication]
