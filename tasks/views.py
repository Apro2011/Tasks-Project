from django.shortcuts import render
from tasks.models import Tasks
from tasks.serializers import TasksSerializer
from rest_framework import generics


# Create your views here.
class TasksList(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class TasksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
