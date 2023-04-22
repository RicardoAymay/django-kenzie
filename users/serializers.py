from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=127)
    username = serializers.CharField(max_length=150)
    birthdate = serializers.DateField(allow_null=True, default=None)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def validate_email(self, email):
        user = User.objects.filter(email=email).first()
        if user:
            raise ValidationError("email already registered.")
        return email

    
    def validate_username(self, username):
        user = User.objects.filter(username=username).first()
        if user:
            raise ValidationError("username already taken.")
        return username

    def create(self, validated_data: dict) -> User:
        if validated_data['is_employee']:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, write_only = True)
    password = serializers.CharField(write_only=True)
    