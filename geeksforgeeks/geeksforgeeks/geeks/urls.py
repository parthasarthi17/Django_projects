from django.urls import path

from .views import detail_view

urlpatterns = [
    path('<id>', detail_view ),
]
