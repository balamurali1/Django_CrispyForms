from django.shortcuts import render
from enroll import models
from enroll import forms

# Create your views here.

def showinfo(request):
	# if request.method == 'POST':
	# 	fm = forms.StudentRegistration(request.POST)
	# 	if fm.is_valid():
	# 		nm = fm.cleaned_data['name']
	# 		em = fm.cleaned_data['email']
	# 		pw = fm.cleaned_data['password']

	# 		reg = models.User(name=nm,email=em,password=pw)
	# 		reg.save()

	# 		fm=forms.StudentRegistration()

	# else:
	# 	fm=forms.StudentRegistration()

	# return render(request,'enroll/user.html',{'form':fm})	




#particular Instance(record/object) thisukoni danini update cheyali..

	if request.method == 'POST':
		pi = models.User.objects.get(pk=3)

		fm = forms.StudentRegistration(request.POST,instance=pi)
		if fm.is_valid():
			fm.save()

			fm=forms.StudentRegistration()

	else:
		fm=forms.StudentRegistration()

	return render(request,'enroll/user.html',{'form':fm})
