from django.shortcuts import render
from enroll import forms

# Create your views here.

def showinfo(request):
	form = forms.StudentRegistration()
	context = {'fm':form}

	return render(request,'enroll/user.html',context=context)

