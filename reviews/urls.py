from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, MovieListCreate, MovieDetail, ReviewListCreate, ReviewDetail, CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  

    path('movies/', MovieListCreate.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),

    path('reviews/', ReviewListCreate.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    
    path('api/', include(router.urls)),  
]
