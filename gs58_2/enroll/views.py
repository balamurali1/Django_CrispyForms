from django.shortcuts import render
from enroll import forms

# Create your views here.

def showinfo(request):
	if request.method == 'POST':
		fm=forms.StudentRegistration(request.POST)
		if fm.is_valid():
			name = fm.cleaned_data.get('name')
			roll = fm.cleaned_data.get('roll')
			price = fm.cleaned_data.get('price')
			rate = fm.cleaned_data.get('rate')
			comment=fm.cleaned_data.get('comment')
			email = fm.cleaned_data.get('email')
			website = fm.cleaned_data.get('website')
			password=fm.cleaned_data.get('password')
			description=fm.cleaned_data.get('description')
			feedback=fm.cleaned_data.get('feedback')
			notes = fm.cleaned_data.get('notes')
			agree = fm.cleaned_data.get('agree')


			fm=forms.StudentRegistration()

	else:
		fm=forms.StudentRegistration()
	
	return render(request,'enroll/user.html',context={'form':fm})			 
