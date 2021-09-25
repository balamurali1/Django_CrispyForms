from django.db import models


class CustomManager(models.Manager):
	def get_stu_roll_range(self,r1,r2):
		return super().get_queryset().filter(roll__range=(r1,r2)).order_by('id')

'''	
Note:filter(roll__range=(r1,r2)).order_by('id') diniki artham emity ante filter use cheshaka
 data naedi order ga ravali id column ani..		
'''
