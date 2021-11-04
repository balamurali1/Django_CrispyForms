from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #idi Built-in forms,already django ne esthundi..

# Create your views here.

def sign_up(request):
	if request.method == "POST":
		fm = UserCreationForm(request.POST)
		if fm.is_valid(): #fm.is_vald() ante, data anedi valid auvna kada ani idi check chesthundi...
			fm.save() #fm.save() ante database lo save kavali ani artham...
		
		fm=UserCreationForm()

	else:		
		fm=UserCreationForm() #Method=="GET" lo vasthe ee line execute auvthundi..

	return render(request,'enroll/signup.html',{'form':fm})



# ee project lo only 'User ni create(signup/user registration)' cheyadam okay na..