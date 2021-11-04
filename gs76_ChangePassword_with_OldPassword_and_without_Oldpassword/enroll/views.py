from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import SignUpForm
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Signup(user creations/user registrations) Function View
def sign_up(request):
	if request.method == "POST":
		fm = SignUpForm(data=request.POST) #request.POST ante SignUpForm lo unna data fm object ki assign auvthundi
		if fm.is_valid(): #fm.is_vald() ante, data anedi valid auvna kada ani idi check chesthundi...
			messages.success(request,'Account Created Successfully !!')	 
			fm.save() #fm.save() ante database lo save kavali ani artham...
			
		fm=SignUpForm()

	else:		
		fm=SignUpForm() #Method=="GET" lo vasthe ee line execute auvthundi..

	return render(request,'enroll/signup.html',{'form':fm})



# Login View Function
def user_login(request):
	if not request.user.is_authenticated: #ee line 1)login kakunte login kavali ani chuspisthundi,2)alreday login ayye unte malli login cheyamani adagadu..adi direct ga else lo ki velthundi..
		if request.method == "POST":
			fm = AuthenticationForm(request=request,data=request.POST) #ee AuthenticationForm class ni by default gs Django ne esthundi..
			#fm = AuthenticationForm(request.POST) #ela rasthe ikkada profile html file lo ki povadam ledu..
			if fm.is_valid():
				uname = fm.cleaned_data['username'] #internal ga "AuthenticationForm lo unde fields" dictionary format lo key and vales vasthai..
				upass = fm.cleaned_data['password']
				user = authenticate(username=uname,password=upass)
				if user is not None: #ante user empty ga lekunte->True, empty ga unte-->False
					login(request,user)
					messages.success(request,'Logged in Successfully!!')
					return HttpResponseRedirect('/profile/') 
			fm = AuthenticationForm() 		

		else:			
			fm = AuthenticationForm()  #method=="GET" lo vasthe ee line execute auvthundi..
		return render(request,'enroll/userlogin.html',{'form':fm})

	else:
		return HttpResponseRedirect('/profile/') #login ayyee n tharuvatha profile page kanipisthundi..	


#Profile

def user_profile(request):
	if request.user.is_authenticated:  #is_authenticated ante credentials(username,Password) unte ne profile page kanapadali ani artham..
		return render(request,'enroll/profile.html',{'name':request.user})

	else:
		return HttpResponseRedirect('/login/')	

# Logout
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')	

#Change Password with old Password
def user_change_pass(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			fm = PasswordChangeForm(user=request.user,data=request.POST)
			if fm.is_valid():
				fm.save()
				update_session_auth_hash(request,fm.user)
				messages.success(request,'Password Changed Successfully!!')
				return HttpResponseRedirect('/profile/')
		else:		
			fm = PasswordChangeForm(user=request.user) #method=='GET' form lo peddithey ee line execute auvthundi...
		return render(request,'enroll/changepass.html',{'form':fm})

	else:
		return HttpResponseRedirect('/login/')






#Change Password without old Password
def user_change_pass1(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			fm = SetPasswordForm(user=request.user,data=request.POST)
			if fm.is_valid():
				fm.save()
				update_session_auth_hash(request,fm.user)
				messages.success(request,'Password Changed Successfully!!')
				return HttpResponseRedirect('/profile/')
		else:		
			fm = SetPasswordForm(user=request.user) #method=='GET' form lo peddithey ee line execute auvthundi...
		return render(request,'enroll/changepass1.html',{'form':fm})

	else:
		return HttpResponseRedirect('/login/')			


#request.user--->ante currently login aina person name vasthundi..