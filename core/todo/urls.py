from django.urls import path
from .views import *

app_name = 'todo'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', IndexCreated.as_view(), name='create'),
    path('edit/<int:pk>/', IndexUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', IndexDelete.as_view(), name='delete')
]
