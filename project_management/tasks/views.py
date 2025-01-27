from rest_framework import viewsets
from tasks.models import Task
from tasks.serializers import TasksSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    
