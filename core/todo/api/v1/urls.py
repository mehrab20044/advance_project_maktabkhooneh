from django.urls import path, include
from .views import TodoList, CategoryList
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("todo", TodoList, basename="todo")
router.register("category", CategoryList, basename="category")
urlpatterns = router.urls
