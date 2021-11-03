from django.shortcuts import render
from enroll.forms import StudentRegistration
from django.contrib import messages


# Create your views here.

def regi(request):
	messages.info(request,'Now You can Login') #ikkada tags ante,info,success,warning,error
	messages.success(request,'Now You can Login')
	messages.warning(request,'Now You can Login')
	messages.error(request,'Now You can Login')
	fm = StudentRegistration()
	return render(request,'enroll/userregistraction.html',{'form':fm})			


#view.py lo rasina messages ani kuda related html(userregistraction.html) file lo ki velthai..