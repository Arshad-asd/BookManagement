from django.urls import path
from user_app.views import *


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/',UserLoginAPIView.as_view(),name='user-login'),
    path('profile/create/',UserProfileCreateAPIView.as_view(),name='user-profile-create'),
    path('profile/update/',UserProfileUpdateAPIView.as_view(),name='user-profile-update'),
]
