from django.shortcuts import render
from main.models import Todo
from main.serializers import CreateToDoSerializer

from rest_framework import generics
# Create your views here.


class CreateToDoView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = CreateToDoSerializer

class ListTodoView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = CreateToDoSerializer
    