from rest_framework.views import APIView, Request, Response, status
from users.models import User
from users.serializers import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    def post(self, request: Request):
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status.HTTP_200_OK)


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)

        if request.user == user or request.user.is_employee:
            serializer = UserSerializer(user)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({"detail": "You do not have permission to perform this action."}, status.HTTP_403_FORBIDDEN)

    def patch(self, request: Request, user_id: int) -> Response:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            if request.user.is_employee == True or request.user.id == user.id:
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            else:
                 return Response({"detail": "You do not have permission to perform this action."}, status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status.HTTP_403_FORBIDDEN)
