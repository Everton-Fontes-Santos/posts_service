from django.urls import path
from .views import index
from .api import router

urlpatterns = [
    path('', index)
]
