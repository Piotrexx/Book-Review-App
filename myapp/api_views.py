from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import generics
from .serializers import *


class AllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookAndContributors(generics.ListAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer