
from rest_framework import permissions
import ipdb
from rest_framework.views import Request, View
from .models import User

class IsEmployee(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_employee == True:
            return True
        
        return False


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view: View, user: User) -> bool:
        if request.user.is_authenticated and request.user.is_employee == True:
            return True
        elif request.user.is_authenticated and request.user == user:
            return True

