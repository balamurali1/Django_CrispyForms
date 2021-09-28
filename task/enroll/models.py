from django.db import models
from django.utils import timezone 

# Create your models here..

class Student_list_table(models.Model):
	name = models.CharField(max_length=200)
	roll_number = models.IntegerField(unique=False)
	date_of_birth = models.DateField(default=timezone.now)

	def __str__(self):
		return self.name

			
 
class Student_mark_table(models.Model):
	student = models.ForeignKey(Student_list_table,on_delete=models.CASCADE)
	marks = models.IntegerField()

	def __str__(self):
		return str(self.marks)	
