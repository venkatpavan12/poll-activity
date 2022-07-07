from django.contrib import admin
from django.urls import path,include
from .views import Homepage,CreatePoll,PollDetail
urlpatterns = [
    path('',Homepage,name='home'),
    path('create-poll',CreatePoll.as_view(),name='create-poll'),
    path('poll/<int:id>',PollDetail,name='poll')
]
