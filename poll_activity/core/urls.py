from django.urls import path,include
from .views import Register,Profile
urlpatterns = [
    path('register/',Register,name='register'),
    path('profile/',Profile,name='profile'),
]
