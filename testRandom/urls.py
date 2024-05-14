from django.contrib import admin
from django.urls import path
from testRandom.views import generate_test
from .views import UserRegistrationAPIView


urlpatterns = [
    path('generate_test/',generate_test , name='generate_test'),
    path('register_user/', UserRegistrationAPIView.as_view(), name='register_user'),
    # Other URL patterns...
]