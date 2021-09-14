from django.shortcuts import render
from enroll.models import User
from enroll.forms import StudentRegistration

# Create your views here.
def showinfo(request):
	if request.method == "POST":
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			nm = fm.cleaned_data['name']
			em = fm.cleaned_data['email']
			pw = fm.cleaned_data['password']

#Insert Process
			# rem = User(name=nm,email=em,password=pw)
			# rem.save()
#UpdateProcess
			# rem = User(id=1,name=nm,email=em,password=pw)
			# rem.save()
#DeleteProcess
			rem = User(id=3)
			rem.delete()			


			fm = StudentRegistration()
	else:
		fm=StudentRegistration()

	return render(request,'enroll/user.html',{'form':fm})

