from django.db import models
from django.db.models import Avg


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def count_movies_d(self):
        return self.movie_d.all().count()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movie_d')

    def __str__(self):
        return self.title

    def rating(self):
        return Review.objects.filter(movies=self).aggregate(Avg('stars'))



class Review(models.Model):
    STARS_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    text = models.TextField()
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='movies_s')
    stars = models.IntegerField(choices=STARS_CHOICE, null=True)










