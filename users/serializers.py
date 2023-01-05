from rest_framework import serializers
from .models import User
import ipdb

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=127)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True)
    is_employee = serializers.BooleanField(default=False)
    password = serializers.CharField(write_only=True)
    id = serializers.IntegerField(read_only=True)

    def validate_email(self, email):
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError("email already registered.")

        return email

    def validate_username(self, username):
        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError("username already taken.")
        
        return username

    def create(self, validated_data):
        # ipdb.set_trace()

        if validated_data['is_employee'] == True:
            user = User.objects.create_superuser(**validated_data)
        elif validated_data['is_employee'] == False: 
            user =  User.objects.create_user(**validated_data)

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)


