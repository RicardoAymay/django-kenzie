from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status
from .models import Movie
from .serializers import MovieSerializer
from users.permissions import IsEmployee
from movies.permissions import IsMovieOwner

class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class GetOneMovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    def get(self, request: Request, movie_id) -> Response:
            movie = Movie.objects.get(id = movie_id)
            
            if self.authentication_classes == False:
                return Response(
                {"detail": "Authentication credentials were not provided."}, status.HTTP_401_UNAUTHORIZED
                )
            return Response(movie)

    def delete(self, request: Request, movie_id) -> Response:

            movie = Movie.objects.get(id = movie_id)

            movie.delete()

            return Response(204)

class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsMovieOwner]

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
