from django.urls import path, include
from .views import *

app_name = 'todo'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', IndexCreated.as_view(), name='create'),
    path('edit/<int:pk>/', IndexUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', IndexDelete.as_view(), name='delete'),
    path("api/v1/",include('todo.api.v1.urls'), name='api-v1')
]
