from rest_framework import permissions
from rest_framework.views import Request, View
from movies.models import MovieOrder, Movie
from .models import User

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View)-> bool:
        return( 
            request.method in permissions.SAFE_METHODS 
            or request.user.is_authenticated 
            and request.user.is_superuser
        )

class IsMovieOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: MovieOrder):
        return obj.user == request.user

class IsProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return obj == request.user