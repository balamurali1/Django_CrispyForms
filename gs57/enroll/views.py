from django.shortcuts import render
from enroll import forms

# Create your views here.

def showinfo(request):
	if request.method == "POST":
		fm = forms.StudentRegistration(request.POST)
		if fm.is_valid():
			print('Form Valid')
			name = fm.cleaned_data['name']
			email = fm.cleaned_data['email']

			return render(request,'enroll/success.html',{'nm':name}) #ela rasthe url name change kadu..!!same url lo ne vasthungi data..


	else:
		fm = forms.StudentRegistration()

	return render(request,'enroll/user.html',{'form':fm})			