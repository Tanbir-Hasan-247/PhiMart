# from rest_framework.permissions import BasePermission
from rest_framework import permissions
from order.models import Cart

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class IsCartOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        cart_id = view.kwargs.get('cart_pk')
        if not cart_id:
            return False
        try:
            cart = Cart.objects.get(pk=cart_id)
        except Cart.DoesNotExist:
            return False
        return cart.user == request.user