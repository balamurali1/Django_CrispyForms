from django.shortcuts import render
from enroll.models import Student
from django.db.models import Avg,Sum,Min,Max,Count

# Create your views here.

def home(request):

	###### all()###########	
	student_data = Student.objects.all() 

	######### Aggregation Avg,Sum,Min,Max,Count #########
	'''
	student_data = Student.objects.all().aggregate(Avg('marks'))
	student_data = Student.objects.all().aggregate(Sum('marks'))
	student_data = Student.objects.all().aggregate(Min('marks'))
	student_data = Student.objects.all().aggregate(Max('marks'))
	student_data = Student.objects.all().aggregate(Count('marks'))
	'''
			#(OR)
	average = student_data.aggregate(Avg('marks'))
	total = student_data.aggregate(Sum('marks'))
	minimum = student_data.aggregate(Min('marks'))
	maximum = student_data.aggregate(Max('marks'))
	count = student_data.aggregate(Count('marks'))


	context = {'data':'Student','student':student_data,
				'average':average,
				'total':total,
				'minimum':minimum,
				'maximum':maximum,
				'count':count}

	print(average)
	print('Reutrn:',student_data)
	print()
	print('SQL Query:',student_data.query)
	return render(request,'enroll/home.html',context)
 