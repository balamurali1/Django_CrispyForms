from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	#user = models.ForeignKey(User,on_delete=models.CASCADE)
	#user = models.ForeignKey(User,on_delete=models.PROTECT)
	user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
	post_title = models.CharField(max_length=70)
	post_category = models.CharField(max_length=70)
	post_publish_date=models.DateField()


'''
Note:1.SET_NULL,pettina tharuvatha compalsary null=True ani pettali pakkane.
2.SET_NULL petti,User table lo oka record ni delete chesthe daniki related unna
chaild table lo ni record lo null ani (-)ela vasthundi.
'''
