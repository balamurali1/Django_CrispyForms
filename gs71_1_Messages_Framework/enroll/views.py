from django.shortcuts import render
from enroll.forms import StudentRegistration
from django.contrib import messages


# Create your views here.

def regi(request):
	if request.method == 'POST':
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			fm.save()
			#messages.success(request,'your Account has been created!!')

			messages.info(request,'Now you can login!!')
			print(messages.get_level(request)) #ela rasthe already unna INFO yooka "default value" yenthano chupisthundi..


			messages.debug(request,'This is Debug')
			messages.set_level(request,messages.DEBUG)
			messages.debug(request,'This is new Debug')
			print(messages.get_level(request))


		fm = StudentRegistration()
	
	else:
		fm=StudentRegistration()
	return render(request,'enroll/userregistraction.html',{'form':fm})			


#view.py lo rasina messages ani kuda related html(userregistraction.html) file lo ki velthai..