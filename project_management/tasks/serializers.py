from rest_framework import serializers
from tasks.models import Task

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description','user','completed','created_at']

# class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    
#     class Meta:
#         model = Categories
#         fields = ['url', 'title', 'tasks']