from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import permissions

class StudentOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_student()
        return True
