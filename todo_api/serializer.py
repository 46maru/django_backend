from rest_framework import serializers # type: ignore
from .models import Todo

class TodoSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'todo', 'completed']