from django.shortcuts import render
from enroll.forms import StudentRegistration
from django.contrib import messages


# Create your views here.

def regi(request):
	if request.method == 'POST':
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			fm.save()
			#messages.add_message(request,messages.SUCCESS, 'your Account has been created!!') #views.py lo only message rasthamu,display cheyali ante html file lo rayali..
			#messages.add_message(request,messages.INFO, 'your Account has been created!!')
				#(OR)
			messages.success(request,'your Account has been created!!')
			messages.info(request,'Now you can login!!')	
		fm = StudentRegistration()
	
	else:
		fm=StudentRegistration()
	return render(request,'enroll/userregistraction.html',{'form':fm})			


#view.py lo rasina messages ani kuda related html(userregistraction.html) file lo ki velthai..