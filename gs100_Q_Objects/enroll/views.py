from django.shortcuts import render
from enroll.models import Student
from django.db.models import Q

# Create your views here.

def home(request):

	########## all() ##########

	#student_date = Student.objects.all()

	######## & #########
	#student_date = Student.objects.filter(Q(id=6) & Q(roll=106))

	#student_date = Student.objects.filter(Q(name='Ramesh') & Q(marks=56))

	#student_date = Student.objects.filter(Q(id=2) & Q(marks=50)) # record not visible because both are not True


	################ | ##############

	#student_date = Student.objects.filter(Q(id =3) | Q(roll=108))

	#student_date = Student.objects.filter(Q(marks = 89) | Q(city='kurnool'))
	
	#student_date = Student.objects.filter(Q(marks =45) | Q(city='Hyderand'))

	#student_date = Student.objects.filter(Q(marks =45) | Q(name = 'Murali'))

	
	############## ~ (Negation Operator) ################

#Note: ~ (Negation Operator) it is particular record not visible in the table

	student_date = Student.objects.filter(~Q(id =3))

	#student_date = Student.objects.filter(~Q(id =1))


	print("Return:",student_date)
	print()
	print('SQL Query:',student_date.query)

	return render (request,'enroll/home.html',context={'student':student_date})
