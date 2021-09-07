from django.shortcuts import render
from enroll import forms


def first(request):
	#if request.method == 'POST':
	if request.POST.get('logpage'): #multiple html pages unnappudu ela if condition first line ela rayali...
		fm = forms.Student(request.POST)
		if fm.is_valid():
			print("Form is Valid!!")
			name = fm.cleaned_data['name']

			return render(request,'enroll/page2.html',{'nm':name})

	if request.POST.get('signpage'):
		fm = forms.Student(request.POST)
		if fm.is_valid():
			print("Form is Valid!!")
			name = fm.cleaned_data['name']
			
			return render(request,'enroll/page3.html',{'nm':name})		

	else:
		fm =forms.Student()		
	return render(request,'enroll/page1.html',context={'form':fm})			
			