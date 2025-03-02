from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    MovieListCreate, MovieDetail,
    ReviewListCreate, ReviewDetail,
    RegisterView, CategoryViewSet, GenreViewSet
)

# Configurare pentru documentația API (Swagger și ReDoc)
schema_view = get_schema_view(
    openapi.Info(
        title="Movies API",
        default_version='v1',
        description="API pentru filme și recenzii",
        terms_of_service="https://www.google.com/policies/terms/",  # Poate fi personalizat
        contact=openapi.Contact(email="contact@moviesapi.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Router pentru viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    # Endpoints pentru filme
    path('movies/', MovieListCreate.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),

    # Endpoints pentru recenzii
    path('reviews/', ReviewListCreate.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # Endpoints pentru autentificare și înregistrare
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),


    # Documentația API (Swagger & ReDoc)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # Adăugarea routerului pentru categorii și genuri
    path('', include(router.urls)),
]
