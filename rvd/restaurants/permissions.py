from rest_framework import permissions

from .models import Restaurant


class IsRestaurantCreator(permissions.BasePermission):
    def has_permission(self, request, view):
        restaurant = Restaurant.objects.get(id=request.data["restaurant"])
        if request.user.id == restaurant.user.id:
            return True
