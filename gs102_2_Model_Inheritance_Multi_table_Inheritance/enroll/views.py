from django.shortcuts import render
from enroll.models import ExamCenter, Student

# Create your views here.

def home(request):
	examcenter_data = ExamCenter.objects.all()
	student_data = Student.objects.all()

	context = {'ex':examcenter_data,
				'stu':student_data}

	return render(request,'enroll/home.html',context = context)
