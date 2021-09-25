from django.db import models
from enroll.managers import CustomManager

# Create your models here.

#Note:proxy ante ne Base class,chaild class Behaviours(data ni artham) same untai.base class yooka 
	#filed's chaild class ki apply auvthai.



class Student(models.Model):
	name = models.CharField(max_length=70)
	roll = models.IntegerField(unique=True,null=False)

class ProxyStudent(Student):
	students = CustomManager()
	class Meta:
		proxy=True  #ela pettinappudu parent lo unde fields ani chaild lo ki vasthai.
		ordering = ['name']	


#Note:proxy gurinchi any information kavali ante gs102_3_Model_Inheritance_Proxy_Model chudu.
