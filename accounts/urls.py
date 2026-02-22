from django.urls import path
from .views import UserList
from .views import UserList, RegisterUser
from .views import LoginUser
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('register/', RegisterUser.as_view(), name='register-user'),
    path('login/', LoginUser.as_view(), name='login-user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]