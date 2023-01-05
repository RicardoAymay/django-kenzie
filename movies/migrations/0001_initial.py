# Generated by Django 4.1.4 on 2023-01-04 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("G", "G"),
                            ("PG", "PG"),
                            ("PG-13", "PG-13"),
                            ("R", "R"),
                            ("NC-17", "NC-17"),
                        ],
                        default="G",
                        max_length=20,
                    ),
                ),
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(default=True, max_length=10, null=True)),
                ("synopsis", models.TextField(default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="MovieOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("buyed_at", models.DateTimeField(auto_now_add=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movie_order",
                        to="movies.movie",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_movie_order",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="movie",
            name="orders",
            field=models.ManyToManyField(
                related_name="user",
                through="movies.MovieOrder",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movies",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
