from django.db import models

# Create your models here.

class CommonInfo(models.Model):
	name = models.CharField(max_length=70)
	age = models.IntegerField()
	date = models.DateField()
	class Meta:
		abstract = True #ela True pedithey base class lo ni field's ani chaild class lo velthai..
#Note: CommonInfo anedi Base class(parent class) kani idi table ga create kadu okay..

class Student(CommonInfo):
	fees = models.IntegerField()
	date = None

#Note: Base class lo ni  niku vadhu anukuna field ni  chaild class lo base class field name  echi None ani apply cheyali	


class Teacher(CommonInfo):
	salary = models.IntegerField()

class Contractor(CommonInfo):
	date = models.DateTimeField() #Base class lo unde field ni chaild class lo ikkada 'inheritance' cheyadam..	
	payment = models.IntegerField()

