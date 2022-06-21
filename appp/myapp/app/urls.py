from django.urls import path
from .views import index, details

urlpatterns = [
    path('', index),
    path('<id>', details),
]
