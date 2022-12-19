from rest_framework import serializers
from .models import Movie, MovieOrder
from users.models import User
import ipdb
class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=True, allow_null=True)
    rating = serializers.CharField(max_length=20)
    synopsis = serializers.CharField(default=True, allow_null=True)
    added_by = serializers.SerializerMethodField()

    def get_owner_email(self, obj: User):
        
        return obj.email

    def create(self, validated_data):
        
        movie = Movie.objects.create(**validated_data)

        return movie


class MovieOrderSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.SerializerMethodField()

    def get_movie_title(self, obj: MovieOrder) -> dict:
        return {"title": obj.movie.title,
                "buyed_by": obj.movie.user,
                "buyed_at": obj.movie.buyed_at
                }
    
    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)