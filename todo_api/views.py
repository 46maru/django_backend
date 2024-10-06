from rest_framework import viewsets, filters
from .models import Todo
from .serializer import TodoSerialiser

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser
    