from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name='category')
	product_name = models.CharField(max_length=100)
	desc = models.TextField()	
	create_date=models.DateTimeField()

	def __str__(self):
		return self.product_name

'''
on_delete=models.PROTECT
Deleting the selected category would require deleting the following protected related objects:
(ఎంచుకున్న వర్గాన్ని తొలగించడానికి కింది రక్షిత సంబంధిత వస్తువులను తొలగించాల్సి ఉంటుంది:)
'''