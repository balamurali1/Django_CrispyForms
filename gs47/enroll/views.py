from django.shortcuts import render
from enroll import forms  

# Create your views here.

def showinfo(request):
	#fm = forms.StudentRegistration(auto_id='some_%s')

	#fm = forms.StudentRegistration(auto_id=True)
				#(OR)
	#fm = forms.StudentRegistration(auto_id="geeky")	

	#fm = forms.StudentRegistration(auto_id=False)

	fm = forms.StudentRegistration(auto_id=True,label_suffix=':',
		initial={'name':'--Name--','email':'--@gmail.com--','first_name':'--First Name--'})	
	
	
	context = {'form':fm}
	return render(request,'enroll/userregistration.html',context = context)
