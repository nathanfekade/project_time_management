from django.contrib.auth.models import User
from rest_framework import serializers
from tasks.models import Task
from tasks.serializers import TasksSerializer


class UserSerializer(serializers.ModelSerializer):

    tasks = TasksSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']


