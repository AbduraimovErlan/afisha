from rest_framework import serializers
from movie_app.models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = 'id name count_movies_d'.split()




class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = 'id title duration director rating'.split()




class ReviewSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()



    class Meta:
        model = Review
        fields = 'id movies stars '.split()

    def get_movies(self, movie):
        return movie.movies.title



