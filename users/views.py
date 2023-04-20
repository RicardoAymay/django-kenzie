from rest_framework.views import APIView, Request, Response, status
from users.models import User
from users.serializers import UserSerializer
class UserView(APIView):

    def get(self, request: Request, Response) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True) 
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data) #passar os dados no serializer
        serializer.is_valid(raise_exception=True) #chamar o validador
       
        serializer.save() #vai chamar o create

        return Response(serializer.data, status.HTTP_201_CREATED)
