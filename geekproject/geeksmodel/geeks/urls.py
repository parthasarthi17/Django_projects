from django.urls import path
from geeks.views import detailsviews, listview

app_name ='geeks'

urlpatterns = [
    path('<int:id>', detailsviews, name= 'detail'),
    path('', listview, name ='GeeksModels_list'),
]
