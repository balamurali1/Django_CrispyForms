from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(default='uncategorized',max_length=100)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')	
	product_name = models.CharField(max_length=100)
	desc = models.TextField()
	create_date=models.DateTimeField(auto_now=True)
	#create_date=models.DateTimeField()

	def __str__(self):
		return self.product_name


