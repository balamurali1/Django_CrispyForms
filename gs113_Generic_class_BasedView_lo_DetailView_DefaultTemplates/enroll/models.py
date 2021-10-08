from django.db import models


# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=70)
	roll = models.IntegerField(unique=True,null=False)
	course = models.CharField(max_length=70)
	