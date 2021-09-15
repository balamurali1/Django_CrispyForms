from django.shortcuts import render

# Create your views here.

def home(request,check): #check anedi main urls lo unde key ni ikkada euvvali 
	print(check)  #idi cmd lo print auvthundi
	context = {'fm':check} #check ni key ki assing chesha nu..
	return render(request,'enroll/home.html',context)

def show(request,my_id):
	if my_id == 1:
		student = {'id':my_id,'name':'Rohan'}

	if my_id == 2:
		student = {'id':my_id,'name':'sonam'}

	if my_id == 3:
		student = {'id':my_id,'name':'murali'}

	return render(request,'enroll/show.html', student)	


def showinfo(request,my_id,my_subid):
	if my_id == 1 and my_subid == 5:
		student = {'id':my_id,'name':'Rohan','info':'Rohan Sub Details'}

	if my_id == 2 and my_subid == 6:
		student = {'id':my_id,'name':'sonam','info':' Sonam Sub Details'}

	if my_id == 3 and my_subid == 7:
		student = {'id':my_id,'name':'murali','info':' murali Sub Details'}

	return render(request,'enroll/show.html', student)		