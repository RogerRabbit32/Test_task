from django.urls import path
from .views import *


urlpatterns = [
    path('auth/register', CreateUser.as_view()),
    path('auth/login', UserLogin.as_view()),
    path('user', UserDetail.as_view()),
]
