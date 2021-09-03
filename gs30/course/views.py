from django.shortcuts import render

# Create your views here.

def learn_django(request):
	context = {'coursename':'Django/Python'}
	return render(request,'course/courseone.html',context = context)
