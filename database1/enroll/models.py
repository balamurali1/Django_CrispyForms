from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=70)
	age = models.IntegerField()

class Address(models.Model):
	city = models.CharField(max_length=70)
	phone = models.IntegerField(unique=True,null=False)
