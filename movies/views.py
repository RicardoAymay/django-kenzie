from rest_framework.views import APIView, Request, Response, status
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2  

class MovieListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request: Request) -> Response:
        movies = Movie.objects.all().order_by('id')
        paginator = CustomPageNumberPagination()
        paginated_movies = paginator.paginate_queryset(movies, request)
        serializer = MovieSerializer(paginated_movies, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)

class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id: int) -> Response:
        try:
            movie = Movie.objects.get(id=movie_id)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self, request: Request, movie_id: int) -> Response:
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

