"""buster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from users.views import UserView, LoginView, GetOneUserView
from rest_framework_simplejwt import views
from movies.views  import MovieView, GetOneMovieView, MovieOrderView

urlpatterns = [
    path("token/", views.TokenObtainPairView.as_view()),  
    path("token/refresh/", views.TokenRefreshView.as_view()),
    path("api/users/", UserView.as_view()),
    path("api/users/login/", LoginView.as_view()),
    path("api/movies/", MovieView.as_view()),
    path("api/movies/<int:movie_id>/", GetOneMovieView.as_view()),
    path("api/movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
    path("api/users/<int:user_id>/", GetOneUserView.as_view())
    
]
