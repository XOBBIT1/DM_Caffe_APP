from rest_framework import permissions


class IsAdminReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(f"_____________________{request.client}________________")
        return bool(request.client and request.client.is_admin)
