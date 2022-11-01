from rest_framework import permissions


class AdminAllManagerAllExceptCreateStaffView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 1:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "PATCH" and request.user.role == 2:
            return True
        return False
