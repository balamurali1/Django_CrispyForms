from django.shortcuts import render
from enroll import forms

# Create your views here.
def showinfo(request):
	if request.method == 'POST':
		fm=forms.StudentRegistration(request.POST)
		if fm.is_valid():
			name = fm.cleaned_data['name']
			email = fm.cleaned_data['email']
			password = fm.cleaned_data['password']

			fm=forms.StudentRegistration()

	else:
		fm=forms.StudentRegistration()

	return render(request,'enroll/user.html',{'form':fm})			
