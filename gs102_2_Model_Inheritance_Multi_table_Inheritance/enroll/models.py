from django.db import models

# Create your models here.

#MultiTable Inheritance(one to one relation)
#Superclass or Base class or Parent class

class ExamCenter(models.Model):
	cname = models.CharField(max_length=70)
	city = models.CharField(max_length=70)


class Student(ExamCenter):
	name = models.CharField(max_length=70)
	roll = models.IntegerField(unique=True,null=False)	
'''
Note:Multiple Inheritance(one to one relation) ante chaild table lo ki parent table ni
Inheritance cheshamu kada appudu parent lo unde field kuda chaild lo ki vasthai kada..
appudu chaild table lo  data enter chesthe automatice ga parent table lo unde related  fields lo ki data
vasthundi...dinine one to one relation antaru.

admin.py lo list_display enduku kante admin.site lo order ga kanipinchadaniki 
'''

