from django.db import models

# Create your models here.

class Category(models.Model):  #This is Parent Table Anuko... 
	name = models.CharField(max_length=100)
	is_active = models.BooleanField(default=True)
	#is_active = models.BooleanField(default=False)

	def __str__(self):
		return self.name

#is_active(default=True) idi yee table rasthe haa table lo unde fields ani active lo unnai ani artham vasthundi.
#is_active(default=False) idi yee table rasthe haa table lo unde fields ani active lo leuve ani artham vasthundi..kani
				#mana mu record create chese samayam lo default=False unna dani, checkbox meeda tick mark apply chesthe
				#internal ga True(active) auvthundi ani...


#parent table lo unde primary key chaild table lo vache sariki Foreignkey ga  change auvthundi...		


class Product(models.Model): #This is Chaild Table Anuko....
	category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
	product_name = models.CharField(max_length=120)
	desc = models.TextField()
	created_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.product_name

