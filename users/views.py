from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsEmployee, IsUser
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
import ipdb
class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if not user:
            return Response(
                {"detail": "No active account found with the given credentials"}, status.HTTP_403_FORBIDDEN
            )

        refresh = RefreshToken.for_user(user)

        token = {"refresh": str(refresh), "access": str(refresh.access_token)}

        return Response(token)

class GetOneUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUser]

    def get(self, request: Request, user_id) -> Response:

        user = get_object_or_404(User, id = user_id)
        self.check_object_permissions(request, user)
        # ipdb.set_trace()
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)