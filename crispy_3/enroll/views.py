from django.shortcuts import render
from enroll.forms import AddressFrom

# Create your views here.

def showinfo(request):
	fm = AddressFrom()
	return render(request,'enroll/form.html',{'form':fm})
