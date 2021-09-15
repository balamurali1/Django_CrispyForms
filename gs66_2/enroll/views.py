from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'enroll/home.html')

def show(request,my_id):
	if my_id == '1':
		student = {'id':my_id,'name':'Rohan'}

	if my_id == '2':
		student = {'id':my_id,'name':'sonam'}

	if my_id == '3':
		student = {'id':my_id,'name':'murali'}

	return render(request,'enroll/show.html', student)	