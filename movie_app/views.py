from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieCreateUpdateSerializer, \
    DirectorCreateUpdateSerializer, ReviewCreateUpdateSerializer
from movie_app.models import *
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from movie_app.models import Review
from movie_app.serializers import ReviewSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer







class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination
    filter_fields = ['name']

class DirectorUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
        queryset = Director.objects.all()
        serializer_class = DirectorSerializer
        lookup_field = 'id'







class MovieListCreateAPIView(ListCreateAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        pagination_class = PageNumberPagination
        filter_fields = ['title', 'description']

class MovieUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        lookup_field = 'id'







class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    filter_fields = ['text', 'stars']

class ReviewUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'









class RegisterAPIView(GenericAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(data={'message': 'User created'}, status=status.HTTP_201_CREATED)



# class AuthorizationAPIView(GenericAPIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#
#     def get(self, request, format=None):
#         return Response({'detail': "I suppose you are authenticated"})
#


class AuthorizationAPIView(GenericAPIView):

    def post(self, request):
        if request.method == "POST":
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                try:
                    token = Token.objects.get(user=user)
                except Token.DoesNotExist:
                    token = Token.objects.create(user=user)
                return Response(data={'key': token.key})
            return Response(data={'error': 'User not found'},
                        status=status.HTTP_404_NOT_FOUND)



