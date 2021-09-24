from django.shortcuts import render
from enroll.models import Student

# Create your views here.

def home(request):

	#student_data = Student.objects.all() #but idi panicheyadu endukante 'objects' name change cheshamu.

	student_data = Student.students.all()
		
	context = {'student':student_data}

	return render(request,'enroll/home.html',context = context)
