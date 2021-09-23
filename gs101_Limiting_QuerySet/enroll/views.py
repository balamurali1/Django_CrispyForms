from django.shortcuts import render
from enroll.models import Student

# Create your views here.

def home(request):
	#student_data = Student.objects.all()

	#student_data = Student.objects.all()[:5]

	#student_data = Student.objects.all()[5:10]

	#student_data = Student.objects.all()[-1] #This is not valid.s

	#student_data = Student.objects.all()[0:10:2]
				#(OR)
	student_data = Student.objects.all()[:10:2]	# :10 mundara by default 0 untundi okay		

	

	print("Return:",student_data)
	

	return render(request,'enroll/home.html',context={'data':'Hello','student':student_data})
