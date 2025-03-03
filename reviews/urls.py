from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, MovieListCreate, MovieDetail, ReviewListCreate, ReviewDetail, CategoryViewSet, GenreViewSet

# Router pentru viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    # Rutele pentru autentificare 
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    # Rutele pentru filme
    path('movies/', MovieListCreate.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),

    # Rutele pentru recenzii
    path('reviews/', ReviewListCreate.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # Rutele pentru categorii și genuri (prin router)
    path('api/', include(router.urls)),  
]
