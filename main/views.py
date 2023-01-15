from django.shortcuts import render
from main.models import Todo
from rest_framework.response import Response
from main.serializers import CreateToDoSerializer

from rest_framework import generics
# Create your views here.


class CreateToDoView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = CreateToDoSerializer

class ListTodoView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = CreateToDoSerializer
    

class RetrieveTodoView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = CreateToDoSerializer

class DestroyTodoView(generics.DestroyAPIView):
    # queryset = Todo.objects.all()
    serializer_class = CreateToDoSerializer

    def delete(self, request, *args, **kwargs):
        todo =Todo.objects.get(id=pk)
        # i.delete()
        return Response({'ALL':'DELETED'})

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)