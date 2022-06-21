from django.urls import path
from .views import index, personview, checkview

urlpatterns = [
    path('', index, name='index'),
    path('<str:name>/', personview, name='peeps'),
    path('check/<str:name>/', checkview, name='checking'),
]
