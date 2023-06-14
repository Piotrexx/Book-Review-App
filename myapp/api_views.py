from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from rest_framework import generics
from .serializers import BookSerializers, PublisherSerializer


@api_view()
def first_api_view(request):
    num_books = Book.objects.count()
    return Response({'num_books':num_books})

# @api_view()
# def all_books(request):
#     books = Book.objects.all()
#     book_serializer = BookSerializers(books, many=True)
#     return Response(book_serializer.data)


class AllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
