from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=70)
	age = models.IntegerField()

class Address(models.Model):
	city = models.CharField(max_length=70)
	phone = models.IntegerField(unique=True,null=False)

"""
MySQL stop lo unnappudu appudu nuvv..Type here to search--->Services-->MySQl80 meeda click chesi
left side 'start'option vasthundi dani meeda click chesthe 'Running' auvthundi..
final ga window ni close cheai..
"""