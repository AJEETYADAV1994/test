from django.db import models


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    fee=models.IntegerField(blank=True,null=True)
    department=models.CharField(max_length=100)
    rate=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    fee=models.IntegerField(blank=True,null=True)
    department=models.CharField(max_length=100)
    rate=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.name

