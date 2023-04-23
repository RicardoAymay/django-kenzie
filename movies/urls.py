from django.urls import path
from .views import MovieListView, MovieDetailView, MovieOrderView

urlpatterns = [
    path('movies/', MovieListView.as_view()),
    path('movies/<int:movie_id>/', MovieDetailView.as_view()),
    path('movies/<int:movie_id>/orders/', MovieOrderView.as_view())       
]
