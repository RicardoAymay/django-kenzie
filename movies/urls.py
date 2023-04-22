from django.urls import path
from . import views
from .views import MovieListView, MovieDetailView




urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movies/<int:movie_id>/', MovieDetailView.as_view(), name='movie-detail'),
]
