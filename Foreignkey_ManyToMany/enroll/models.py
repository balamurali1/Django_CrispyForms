from django.db import models

# Create your models here.

#Note:ikkada Prathi daniki null=True Use cheshamu kada..yendukante. yedina field lo data rayakunda vadilesinapudu databse lo Null ani padali anduku rashamu. 



class Customer(models.Model):
	name = models.CharField(max_length=200,null=True)
	phone=models.CharField(max_length=200,null=True)
	email = models.EmailField(max_length=200,null=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.name

class Tag(models.Model): #tag ante thigns(vasthuvulu anuko..)
	name= models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	CATEGORY = (
		('In Door','In Door'),
		('out Door','Out Door'),
		)		

	name=models.CharField(max_length=200,null=True)
	price= models.FloatField(null=True)
	category = models.CharField(max_length=200,null=True,choices=CATEGORY)
	description=models.CharField(max_length=200,null=True,blank=True)
	date_created=models.DateTimeField(auto_now_add=True,null=True)
	tag = models.ManyToManyField(Tag)


	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
		('Pending','Pending'),
		('Out for Delivery', 'Out for Delivery'),
		('Delivered','Delivered'),
		)		
	customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
	product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True,null=True)
	status = models.CharField(max_length=200,null=True,choices=STATUS)
