from django.shortcuts import render
from enroll import forms
from enroll.models import User

# Create your views here.

def showinfo(request):
	if request.method == 'POST':
		fm = forms.StudentRegistration(request.POST)
		if fm.is_valid():
			nm = fm.cleaned_data['name']
			em = fm.cleaned_data['email']
			pw = fm.cleaned_data['password']

				#Inser
			# reg = User(name=nm,email=em,password=pw)
			# reg.save()	

				#Update
			# reg = User(id=3,name=nm,email=em,password=pw)
			# reg.save()	

				#delete
			reg = User(id=1)	#form lo yedaina fill chesi submit kottu...table lo delete auvthundi
			reg.delete()	


			fm=forms.StudentRegistration()		

	else:
		fm=forms.StudentRegistration()

	return render(request,'enroll/user.html',{'form':fm})



