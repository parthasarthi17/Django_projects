from django.urls import include, path
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register('heroes', views.HeroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', views.HelloView.as_view(), name='hello'),
]
