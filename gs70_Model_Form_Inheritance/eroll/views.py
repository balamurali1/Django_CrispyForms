from django.shortcuts import render
from eroll.models import User
from eroll.forms import StudentRegistration,TeacherRegistration

# Create your views here.

def student_form(request):
	if request.method=='POST':
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			fm.save()
		fm=StudentRegistration()	

	else:
		fm = StudentRegistration()

	return render(request,'eroll/student.html',{'form':fm})	


def teacher_form(request):
	if request.method == 'POST':
		fm = TeacherRegistration(request.POST)
		if fm.is_valid():
			fm.save()
		fm=StudentRegistration()	

	else:
		fm = TeacherRegistration()

	return render(request,'eroll/teacher.html',{'form':fm})				

