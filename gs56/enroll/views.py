from django.shortcuts import render
from enroll import forms

# Create your views here.

def showinfo(request):
	if request.method == 'POST':
		fm = forms.StudentRegistration(request.POST)
		if fm.is_valid():
			print('Form Validation')
			name = fm.cleaned_data['name']
			email = fm.cleaned_data['email']
			# print('Name:',name)
			# print('Email:',email)
			fm = forms.StudentRegistration() 
				
	else:
		fm = forms.StudentRegistration()

	return render(request,'enroll/user.html',{'form':fm})			