from django.shortcuts import render
from enroll.forms import StudentRegistration

# Create your views here.

def showinfo(request):
	if request.method == 'POST':
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			nm = fm.cleaned_data['name']
			em = fm.cleaned_data['email']
			pw = fm.cleaned_data['password']
			print(nm)
			print(em)
			print(pw)

			fm = StudentRegistration()

	else:
		fm=StudentRegistration()

	return render(request,'enroll/user.html',{'form':fm})						