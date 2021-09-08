from django.shortcuts import render
from enroll import forms

# Create your views here.

def showinfo(request):
	if request.method == 'POST':
		fm = forms.Student(request.POST)
		if fm.is_valid():
			name = fm.cleaned_data['name']
			email = fm.cleaned_data['email']

			fm=forms.Student()

	else:
		fm=forms.Student()


	return render(request,'enroll/user.html',{'form':fm})
					