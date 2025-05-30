from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserDetailView, RegisterView, FileDataViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'files-data', FileDataViewset)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('detail/', UserDetailView.as_view(), name='user-detail'),
    path('register/', RegisterView.as_view(), name='register'),

] + router.urls
