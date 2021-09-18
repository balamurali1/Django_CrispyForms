from django.db import models
from django.contrib.auth.models import User #By default ga User table anedi Database lo Untundi...
from django.utils import timezone

# Create your models here.

class Course(models.Model):
	title = models.CharField(max_length=200)
	place = models.CharField(max_length=200)
	size = models.IntegerField()
	date = models.DateTimeField()
	time = models.TimeField()
	description = models.TextField(max_length=700)
	speaker = models.CharField(max_length=100)
	enterprise = models.CharField(max_length=100)
	photo = models.FileField(null=True)
	more_info=models.FileField(blank=True,null=True)
	file = models.FileField(blank=True,null=True)
	users = models.ManyToManyField(User,blank=True)


