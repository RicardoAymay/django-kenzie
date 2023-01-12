from rest_framework import serializers
from .models import Movie, MovieOrder
from users.models import User
import ipdb
class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=True, allow_null=True)
    rating = serializers.ChoiceField(choices=Movie.options_rating, default=Movie.options_G)
    synopsis = serializers.CharField(default=None, allow_null=True)
    added_by = serializers.SerializerMethodField()
    id = serializers.IntegerField(read_only=True)

    def get_added_by(self, obj: User):
        
        return obj.owner.email

    def create(self, validated_data):
        
        movie = Movie.objects.create(**validated_data)
        
        return movie


class MovieOrderSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    id = serializers.IntegerField(read_only=True)

    def get_title(self, obj: MovieOrder):
        return obj.movie.title

    def get_buyed_by(self, obj: MovieOrder):
        return obj.user.email

    def create(self, validated_data):
        movie = MovieOrder.objects.create(**validated_data)
        return movie

        