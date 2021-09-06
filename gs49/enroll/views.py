from django.shortcuts import render
from enroll import forms

# Create your views here.
def showinfo(request):
	form = forms.StudentRegistration()
	context = {'form':form}
	
	return render(request,'enroll/userregistration.html',context=context)	