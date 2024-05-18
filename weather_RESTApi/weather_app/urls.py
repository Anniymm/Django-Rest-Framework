from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', CreateExternal.as_view(), name='create_external'),
]


