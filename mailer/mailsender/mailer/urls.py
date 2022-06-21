from django.urls import path
from .views import mailsend

urlpatterns = [
    path('', mailsend),

]
