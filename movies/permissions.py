from rest_framework import permissions
from rest_framework.views import Request, View
from movies.models import Movie
from users.models import User
import ipdb


class IsMovieOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, movie: Movie) -> bool:
        return movie.owner == request.user

class IsEmployeeMovie(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:
        if user.is_employee == True:
            return True
        if user.is_employee == False:
            return False