from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Table(models.Model):
    username=models.CharField(max_length=50,null=True,blank=True)
    title=models.CharField(max_length=50,null=False,blank=False)
    description=models.TextField(max_length=5000,null=False,blank=False)
    status=models.BooleanField(default=False)
  
class Use(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.CharField(max_length=50,null=True,blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='replies')
    name=models.CharField(max_length=50,null=False,blank=False)
    message=models.TextField(max_length=5000,null=True,blank=True)
    likes=models.ManyToManyField(User)




