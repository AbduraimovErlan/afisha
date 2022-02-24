from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError



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



class DirectorCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=20)
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        if Director.objects.filter(id=director_id).count() == 0:
            raise ValidationError(f"Category with id={director_id} not found!")
        return director_id


class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=10)
    description = serializers.CharField()
    duration = serializers.DurationField(required=False)
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        if Director.objects.filter(id=director_id).count() == 0:
            raise ValidationError(f"Category with id={director_id} not found!")
        return director_id



class ReviewCreateUpdateSerializer(serializers.Serializer):
    stars = serializers.IntegerField(min_value=int(1), max_value=int(5))
    text = serializers.CharField()
    movies_id = serializers.IntegerField()

    def validate_director_id(self, movies_id):
        if Review.objects.filter(id=movies_id).count() == 0:
            raise ValidationError(f"Category with id={movies_id} not found!")
        return movies_id






