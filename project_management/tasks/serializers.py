from rest_framework import serializers
from tasks.models import Task

class TasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url','title','description','user','completed','created_at']