from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Restaurant
from .serializers import (
    RestaurantSerializer,
    # RestaurantAvgInfoSerializer,
    VisitCreateSerializer,
    UserCreateSerializer,
)
from .permissions import IsRestaurantCreator


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class RestaurantCreateAPIView(generics.CreateAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]


# Option 1
class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]


class RestaurantListAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]


# Option 2
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]


class VisitCreateAPIView(generics.CreateAPIView):
    serializer_class = VisitCreateSerializer
    permission_classes = [IsRestaurantCreator]
