from django.shortcuts import render
from enroll.forms import SignUpForm
from django.contrib import messages 

# Create your views here.

def sign_up(request):
	if request.method == "POST":
		fm = SignUpForm(request.POST)
		if fm.is_valid(): #fm.is_vald() ante, data anedi valid auvna kada ani idi check chesthundi...
			messages.success(request,'Account Created Successfully !!')	 
			fm.save() #fm.save() ante database lo save kavali ani artham...
			
		fm=SignUpForm()

	else:		
		fm=SignUpForm() #Method=="GET" lo vasthe ee line execute auvthundi..

	return render(request,'enroll/signup.html',{'form':fm})


# ee projects lo extra fields(label_tags) ni add cheyadam..
