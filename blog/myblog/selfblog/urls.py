from django.urls import path

from .views import frontView, articlesView

urlpatterns = [
    path('', frontView.as_view(), name="front"),
    path('article/<int:pk>', articlesView.as_view(), name="articlesdetail")
]
