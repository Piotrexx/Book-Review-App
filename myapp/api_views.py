from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

class AllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookAndContributors(generics.ListAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.order_by('-date_created')
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = []