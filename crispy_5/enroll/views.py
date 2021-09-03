from django.shortcuts import render
from enroll import forms
# Create your views here.

# def showinfo(request):
# 	form =forms.AddressFrom()
# 	if request.method == 'POST':
# 		form = forms.AddressFrom(request.POST)
# 		html = "We have recieved this form again"

# 	else:
# 		html = 'Welcome to first time registration'	
# 	return render(request,'enroll/form.html',{'html':html,'form':form})

#				(OR)


def showinfo(request):
	form =forms.AddressFrom()
	if request.method == 'POST':
		form = forms.AddressFrom(request.POST)
		html = "We have recieved this form again"
		if form.is_valid():
			html = html+'This Form is Valid'

	else:
		html = 'Welcome to first time registration'	
	return render(request,'enroll/form.html',{'html':html,'form':form})


