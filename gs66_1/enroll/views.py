from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request,'enroll/user.html')

def show(request,my_id):
	return render(request,'enroll/show.html',{'id':my_id})	