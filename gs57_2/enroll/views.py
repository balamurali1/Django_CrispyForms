from django.shortcuts import render
from django.http import HttpResponseRedirect
from enroll import forms

# Create your views here.
def completed(request):
	return render(request,'enroll/success.html')


def showinfo(request):
	if request.method=='POST':
		fm =forms.StudentRegistration(request.POST)
		if fm.is_valid():
			print("Form Validated!!")

			return HttpResponseRedirect('/regi/success/')


	
	else:
		fm = forms.StudentRegistration()
	return render(request,'enroll/user.html',{'form':fm})		