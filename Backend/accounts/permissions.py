from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["ADMIN", "SUPERUSER"]


class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["SUPERVISOR", "ADMIN", "SUPERUSER"]


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "STAFF"
