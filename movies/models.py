from django.db import models

# Create your models here.
class Movie(models.Model):
        options_G = ("G")
        options_PG = ("PG")
        options_PG13 = ("PG-13")
        options_R = ("R")
        options_NC = ("NC-17")

        options_rating = [
            (options_G, options_G),
            (options_PG, options_PG),
            (options_PG13, options_PG13),
            (options_R, options_R),
            (options_NC, options_NC)
        ]

        rating = models.CharField(max_length=20, choices=options_rating, default="G")
        title = models.CharField(max_length=127)
        duration = models.CharField(max_length=10, default=True, null=True)
        synopsis = models.TextField(default=True, null=True)

        owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
        )

        orders = models.ManyToManyField(
            "users.User",
            through="movies.MovieOrder", 
            related_name="user",
        )


class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_order"
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movie_order"
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
