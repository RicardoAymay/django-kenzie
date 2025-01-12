from django.db import models
from datetime import datetime
class Ratings(models.TextChoices):
    G = 'G',
    PG = 'PG',
    PG_13 = 'PG-13',
    R = 'R'
    NC_17 = 'NC-17'

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, choices=Ratings.choices, default=Ratings.G)
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies"
        )
    users = models.ManyToManyField(
        "users.User",
        through='movies.MovieOrder',
        related_name="movie_orders"
    )
    def __repr__(self) -> str:
        return f'<Movie [{self.id}] - {self.title}>'

class MovieOrder(models.Model):
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete= models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    