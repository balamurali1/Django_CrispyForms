from django.shortcuts import render

# Create your views here.

def learn_python(request):
	return render(request,'course/courseone.html',{'nm':'Python'})
	