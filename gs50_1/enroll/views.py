from django.shortcuts import render
from enroll import forms

# Create your views here.

def showinfo(request):
	fm = forms.StudentRegistration()

	return render(request,'enroll/user.html',context={'form':fm})

	
