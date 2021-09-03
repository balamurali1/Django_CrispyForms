from django.shortcuts import render
from enroll.models import Student

# Create your views here.

def studentinfo(request,id):
	#stud = Student.objects.all()
	stud = Student.objects.get(pk=id)
	return render(request,'enroll/studentone.html',{'stu':stud})
