from django.db import models


# Create your models here.

class Amenity(models.Model):
	name = models.CharField(max_length=30)
	#description = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.name

class Store(models.Model):
	name = models.CharField(max_length=30)
	#address = models.CharField(max_length=30)
	address = models.TextField()
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=20)
	email = models.EmailField()

	def __str__(self):
		return self.name

	#amenity = models.ManyToManyField(Amenity,related_name='amenity',blank=False)	
	amenity = models.ManyToManyField(Amenity,related_name='amenity',blank=True)	