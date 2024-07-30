
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import AccountCreateAPIView

urlpatterns = [
    path('token/,',TokenObtainPairView.as_view(),name = 'token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('signup/', AccountCreateAPIView.as_view(),name='signup'),
]
