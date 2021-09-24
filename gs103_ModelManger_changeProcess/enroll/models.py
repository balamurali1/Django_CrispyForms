from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=70)
	roll = models.IntegerField(unique=True,null=False)
	students = models.Manager() #ela create cheyali new manager ni okay..



'''
Note:
 Ex: student_data = Student.objects.all(), ee line lo unde 'objects'name dinini by default
 ga Manager ani antaru.dinini marchali anukunte class lo "students = models.Manager()"
 ela euvali. appudu manamu database nundi data thisukune time lo objects ni use cheyamu.
 yendukante change cheshamu kada..okay. appudu ela thisukuntamu "student_data = Student.students.all()"
ela rayali command line okay na.. kani dinini admin.py lo list_display lo add cheyakudadu.
vadu anukunte haa field ni remove chesthe saripothundi..malli normal ga vasthundi..
 '''