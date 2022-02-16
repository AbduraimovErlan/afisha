from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    # @property
    # def count_movies(self):
    #     return self.movies.all().count()




class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.DurationField(null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    STARS_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    text = models.TextField()
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    stars = models.CharField(choices=STARS_CHOICE, max_length=100, null=True)








