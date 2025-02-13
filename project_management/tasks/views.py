from rest_framework import viewsets
from tasks.models import Task, Category
from tasks.serializers import TasksSerializer, CategorySerializer, AddTasksToCategoryByTitleSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class TaskList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        tasks = Task.objects.filter(user= request.user)
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=TasksSerializer, responses={201: TasksSerializer})
    def post(self, request, format=None):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class TaskDetail(APIView):
    
    permission_classes = [IsAuthenticated]

    def get_object(self,request ,pk):
        
            return get_object_or_404(Task, pk=pk, user=request.user)


    def get(self, request, pk, format=None):
        task = self.get_object(request, pk)
        serializer = TasksSerializer(task)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=TasksSerializer, responses={200: TasksSerializer})
    def put(self, request, pk, format=None):
        task = self.get_object(request, pk)
        serializer = TasksSerializer(task, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        categories = Category.objects.filter(user = request.user)
        serializer = CategorySerializer(categories, many= True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=CategorySerializer, responses={201: CategorySerializer})
    def post(self, request, format=None):
        serializer = CategorySerializer(data= request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, request , pk):
        
        return get_object_or_404(Category, pk=pk, user=request.user)
    
    def get(self, request, pk, format=None):
        category = self.get_object(request,pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CategorySerializer, responses={200: CategorySerializer})
    def put(self, request, pk, format=None):
        category = self.get_object(request,pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AddTasksToCategory(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, category_id):

        category = get_object_or_404(Category, id=category_id, user=request.user)

        available_tasks = Task.objects.filter(user=request.user).exclude(id__in=category.tasks.all())

        serializer = TasksSerializer(available_tasks, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=AddTasksToCategoryByTitleSerializer, responses={200: "Task added successfully", 400: "Invalid task title"})
    def post(self, request, category_id):
        
        category = get_object_or_404(Category, id=category_id, user=request.user)

        serializer = AddTasksToCategoryByTitleSerializer(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)

        print("Received request data:", request.data)

        tasks = serializer.validated_data['task_titles']

        category.tasks.add(*tasks)

        return Response({"status": f"Added {len(tasks)} tasks to category '{category.title}'."},status=status.HTTP_200_OK)

    
