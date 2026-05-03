from django.db import models
from datetime import datetime
from django.urls import reverse

class TodoModel(models.Model):
    author = models.ForeignKey('accounts.profile',on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    complete = models.BooleanField(default=False)
    category = models.ForeignKey("Category",on_delete=models.SET_NULL,null=True)
   

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.text[:12]
    def get_absolute_api_url(self):
        return reverse('todo:api-v1:todo-detail', kwargs={'pk':self.pk})



class Category(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField(help_text='number for priority in task' ,null=True)

    def __str__(self):
        return f'{self.name}({self.level})' 