from django.urls import path
from . import views
from .views import UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/login/", views.LoginView.as_view()),
    path("users/<int:user_id>/", UserProfileView.as_view()),
    path("token/", TokenObtainPairView.as_view()),  
    path("token/refresh/", TokenRefreshView.as_view()),  
]

