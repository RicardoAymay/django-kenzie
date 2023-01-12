from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer
from users.permissions import IsEmployee
from rest_framework.permissions import IsAuthenticated
from movies.permissions import IsMovieOwner
import ipdb
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from buster.pagination import CustomPageNumberPagination

class MovieView(APIView, CustomPageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request)

        serializer = MovieSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

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

            serializer = MovieSerializer(movie)

            if self.authentication_classes == False:
                return Response(
                {   "detail": "Authentication credentials were not provided."}, status.HTTP_401_UNAUTHORIZED
                )
            return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id) -> Response:

            movie = Movie.objects.get(id = movie_id)

            movie.delete()

            return Response(status=204)

class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id) -> Response:
        # ipdb.set_trace()
        movie_obj = get_object_or_404(Movie, pk=movie_id)
        
        self.check_object_permissions(request, movie_obj)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie = movie_obj, user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
