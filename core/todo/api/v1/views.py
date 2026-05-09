from rest_framework import viewsets
from .serializers import TodoSerializer, CategorySerializer
from ...models import TodoModel, Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TodoList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()


class CategoryList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
