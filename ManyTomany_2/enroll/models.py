from django.db import models

# Create your models here.

class Worker(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Machine(models.Model):
	name = models.CharField(max_length=200)
	worker = models.ManyToManyField(Worker,related_name='worker')

	def __str__(self):
		return self.name