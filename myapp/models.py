from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    list_name = models.CharField(max_length=100, default='Default list name')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class ToDoList(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task_name = models.CharField(max_length=100 )
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)    

    #def __str__(self):
        #return self.task_name    
