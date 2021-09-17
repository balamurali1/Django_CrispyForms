from django.db import models

# Create your models here.

class Customer(models.Model):
	cus_name = models.CharField(max_length=100)
	cus_email = models.EmailField(max_length=100)
	cus_phone=models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.cus_name

class Products(models.Model):
	cus_id=models.ManyToManyField(Customer)
	pro_name = models.CharField(max_length=100)
	pro_qty = models.CharField(max_length=100)

	def __str__(self):
		return self.pro_name
