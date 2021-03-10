from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import permissions

class StudentOnlyPermission(permissions.BasePermission):

    message = "Only students have permission to perform this action."

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_student()
        return True


class TeacherOnlyPermission(permissions.BasePermission):

    message = "Only teachers have permission to perform this action."

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_teacher()
        return True

    def has_object_permission(self, request, view, obj):   
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'PATCH':
            return obj.user == request.user
        else:
            return True
