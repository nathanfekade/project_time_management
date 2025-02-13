from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    user = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        unique_together = ['user', 'title']

    
    def save(self, *args, **kwargs):
        self.full_clean() # validating in both models and serializers incase data was inserted with out using DRF serializsers
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    tasks = models.ManyToManyField(Task, related_name='categories')
    user = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']
        unique_together = ['user','title' ]


    
    def save(self, *args, **kwargs):
        self.full_clean() # validating in both models and serializers incase data was inserted with out using DRF serializsers
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


