from rest_framework import viewsets
from tasks.models import Task
from tasks.serializers import TasksSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=TasksSerializer, responses={201: TasksSerializer})
    def post(self, request, format=None):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class TaskDetail(APIView):
    
    def get_object(self, pk):
        try: 
            return Task.objects.get(pk = pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TasksSerializer(task)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=TasksSerializer, responses={200: TasksSerializer})
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TasksSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    
