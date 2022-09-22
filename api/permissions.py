from rest_framework import permissions

class IsSuperAdmin(permissions.BasePermission):
    """
    Custom permission to allow access to SuperAdmin only
    """
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
