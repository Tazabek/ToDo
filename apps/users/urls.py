from django.urls import path
from .views import UserAPIView, UpdateDataAPIView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register('user', UserAPIView, basename='user')

urlpatterns = [
    path('user/<int:pk>/', UpdateDataAPIView.as_view(), name='update'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
