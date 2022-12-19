
from rest_framework import permissions
import ipdb
from rest_framework.views import Request, View

class IsEmployee(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.IsEmployee:
            return True
        
        return False