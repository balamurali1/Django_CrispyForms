from django.shortcuts import render
from enroll.models import ExamCenter,StudentCenter

# Create your views here.


def home(request):
	examcenter_data = ExamCenter.objects.all()
	Studentcenter_data = StudentCenter.objects.all()

	context = {'exam':examcenter_data,'student':Studentcenter_data}	

	return render(request,'enroll/home.html',context = context)
	
