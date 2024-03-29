"""
URL configuration for rvd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from restaurants.views import (
    RestaurantCreateAPIView,
    RestaurantListAPIView,
    RestaurantRetrieveUpdateDestroyAPIView,
    RestaurantViewSet,
    VisitCreateAPIView,
    UserCreateAPIView,
)

router = routers.SimpleRouter()
router.register(r"restaurant", RestaurantViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Swagger
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # Registration
    path("api/v1/registration/", UserCreateAPIView.as_view()),
    # JWT Token
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Restaurant
    path("api/v1/restaurant_create/", RestaurantCreateAPIView.as_view()),
    # Option 1
    path("api/v1/restaurant_list/", RestaurantListAPIView.as_view()),
    path(
        "api/v1/restaurant_detail/<int:pk>/",
        RestaurantRetrieveUpdateDestroyAPIView.as_view(),
    ),
    # Option 2
    path("api/v1/", include(router.urls)),  # http://127.0.0.1:8000/api/v1/restaurant
    # Option 3
    path("api/v1/restaurant/", RestaurantViewSet.as_view({"get": "list"})),
    path(
        "api/v1/restaurant/<int:pk>/",
        RestaurantViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
            }
        ),
    ),
    # Visit
    path("api/v1/visit_create/", VisitCreateAPIView.as_view()),
]
