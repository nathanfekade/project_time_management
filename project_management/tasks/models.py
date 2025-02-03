from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    user = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

class Categories(models.Model):
    title = models.CharField(max_length=100)
    task = models.ManyToManyField(Task)

    class meta:
        ordering = ['title']
