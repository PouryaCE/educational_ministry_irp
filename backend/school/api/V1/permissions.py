from rest_framework import permissions
from accounts.models import OfficeManager
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is a superuser or official manager
        return request.user.is_admin  # or request.user.is_official manager
        # we should complete this code after fixing registrations


class IsSuperuserOrOfficeManager(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.is_admin:
            return True
        elif request.user.is_authenticated and OfficeManager.objects.filter(id=request.user.id).exists():
            return True
        else:
            return False
