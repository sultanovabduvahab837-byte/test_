from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.pagination import PageNumberPagination


class TaskPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = TaskPagination

    def get_queryset(self):
        queryset = Task.objects.all()
        status_param = self.request.query_params.get('status')

        if status_param == 'true':
            queryset = queryset.filter(is_completed=True)
        elif status_param == 'false':
            queryset = queryset.filter(is_completed=False)

        return queryset


class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]


