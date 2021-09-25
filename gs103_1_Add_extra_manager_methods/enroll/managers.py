from django.db import models

class CustomManager(models.Manager):
	def get_stu_roll_range(self,r1,r2): #r1,r2 ante start to ending rows ani artham
		return super().get_queryset().filter(roll__range=(r1,r2))


'''
Note; idi ni gurinchi thelusukovali ante gs103_Custom_Model_Manager,chudu
clear ga rashanu	
'''	