from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.mixins import PermissionRequiredMixin


class LoginRequiredMixin:
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        JWTAuthentication,
    ]
    permission_classes = [IsAuthenticated]


class PermissionIsStudent(PermissionRequiredMixin):
    def has_permission(self, request, view):
        return hasattr(request.user, "student")


class LoginStudentRequiredMixin:
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        JWTAuthentication,
    ]
    permission_classes = [PermissionIsStudent]
