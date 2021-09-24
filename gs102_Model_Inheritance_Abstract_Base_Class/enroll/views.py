from django.shortcuts import render
from enroll.models import Student,Teacher,Contractor

# Create your views here.

def home(request):
	student_data = Student.objects.all()
	teacher_data = Teacher.objects.all()
	contractor = Contractor.objects.all()

	context = {'student':student_data,'teacher':teacher_data,'contractor':contractor}

	return render(request,'enroll/home.html',context = context)
