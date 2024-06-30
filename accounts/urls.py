from django.urls import path
from accounts.api_views.tokens import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
    TestAuth
)

urlpatterns = [
    path('token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('test', TestAuth.as_view(), name='test_auth')
]