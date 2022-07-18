from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.customer == request.user:
            return True
        return False


class IsItem(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.cart.customer == request.user:
            return True
        return False



