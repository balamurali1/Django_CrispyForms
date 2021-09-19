from django.db import models

# Create your models here.

class Table(models.Model):
	name = models.CharField(max_length=200)
	roll = models.IntegerField(unique=True)
	city = models.CharField(max_length=200,blank=True)
	#vilage = models.CharField(max_length=200,null=True,blank=True)
	vilage = models.CharField(max_length=200,null=True,blank=False)


class Student(models.Model):
	name = models.CharField(max_length=200,null=False)
	roll=models.IntegerField(unique=False)
	city=models.CharField(max_length=200,blank=False)
	#vilage=models.CharField(max_length=200,null=False,blank=False)
	vilage = models.CharField(max_length=200,null=False,blank=True)



