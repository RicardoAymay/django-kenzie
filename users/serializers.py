from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


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

    def update(self, instance, validated_data):
    
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.is_employee = validated_data.get('is_employee', instance.is_employee)
        password = validated_data.get('password')
        if password:
            instance.password = make_password(password)

        instance.save()
        return instance
    
    def create(self, validated_data: dict) -> User:
        if validated_data['is_employee']:
            return User.objects.create_superuser(**validated_data)
    
 

        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, write_only = True)
    password = serializers.CharField(write_only=True)
    