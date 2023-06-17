from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth import authenticate
from rest_framework.authentication import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

class Login(APIView):

    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password")) # getting the username and password of logged user
        if not user:
            return Response({'error': 'Credentails are incorrect or username does not exist'}, status=HTTP_404_NOT_FOUND) # if user isn't logged in then error goes up
        token, _ = Token.objects.get_or_create(user=user) # creating or getting the token that was created
        return Response({'token': token.key}, status=HTTP_200_OK) # if user has the token then te status of request is 200 (is good)


class AllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookAndContributors(generics.ListAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication] # user need to have auth token
    permission_classes = [IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.order_by('-date_created')
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = []