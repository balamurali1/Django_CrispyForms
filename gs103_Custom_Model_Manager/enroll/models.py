from django.db import models
from enroll.managers import CustomManager

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=70)
	roll = models.IntegerField(unique=True,null=False)

	students=CustomManager()

'''
Note:customManager ante manamu own ga create chesukunna Manager,idi supparet ga
managers.py lo create chesukoni ikkada import cheshanu.managers.py lo ne manaku mundugane
result yela ravalo mudugane chepsthamu like nenu echanu chudu order_by['name'] ani,ante
name column lo name ani alphabetical order lo ravali ani echaa..ela..
'''