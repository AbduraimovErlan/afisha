from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from movie_app.models import *
from rest_framework import status


@api_view(["GET"])
def director_list_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)

@api_view(["GET"])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Director not found'})
    director = Director.objects.get(id=id)
    data = DirectorSerializer(director).data
    return Response(data=data)



@api_view(["GET"])
def movie_list_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)

@api_view(["GET"])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Movie not found'})
    movie = Movie.objects.get(id=id)
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(["GET"])
def review_list_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data)

@api_view(["GET"])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Review not found'})
    review = Review.objects.get(id=id)
    data = ReviewSerializer(review).data
    return Response(data=data)