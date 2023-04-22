from rest_framework import serializers
from .models import Ratings, Movie
from users.models import User
import ipdb
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(choices=Ratings.choices, default=Ratings.G)
    synopsis = serializers.CharField(allow_null=True, default = None)
    added_by = serializers.SerializerMethodField(read_only=True)
    user = User()
    
    def get_added_by (self, obj):
        return obj.user.email
    
    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)
