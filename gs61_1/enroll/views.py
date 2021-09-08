from django.shortcuts import render
from enroll import forms

# Create your views here.

def showinfo(request):
	if request.method == 'POST':
		fm = forms.Student(request.POST)
		if fm.is_valid():
			name = fm.cleaned_data.get('name')
			city = fm.cleaned_data.get('city')
			email = fm.cleaned_data.get('email')

			fm = forms.Student()

	else:
		fm=forms.Student()

	return render(request,'enroll/user.html',{'form':fm})

