from django.shortcuts import render
from enroll import forms

# Create your views here.
def showinfo(request):
	if request.method == 'POST':
		fm=forms.StudentRegistration(request.POST)
		if fm.is_valid():
			print('Name:',fm.cleaned_data.get('name'))
			print('Email:',fm.cleaned_data.get('email'))
			print('Password:',fm.cleaned_data.get('password'))

			fm=forms.StudentRegistration()

	else:
		fm=forms.StudentRegistration()

	return render(request,'enroll/user.html',{'form':fm})				
