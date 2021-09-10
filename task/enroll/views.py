from django.shortcuts import render,redirect
from enroll.forms import Student_list,Student_mark
from enroll.models import Student_list_table,Student_mark_table

# Create your views here.
def home1(request):
	data = Student_list_table.objects.all() 
	return render(request,'enroll/home1.html',{'data':data})


def create_stu(request):
	if request.method == "POST":
		fm = Student_list(request.POST)
		if fm.is_valid():
			nm = fm.cleaned_data['name']
			roll = fm.cleaned_data['roll_number']
			dob = fm.cleaned_data['date_of_birth']

			reg = Student_list_table(name=nm,roll_number=roll,date_of_birth=dob)
			reg.save()
			fm = Student_list()
			return redirect("/api/stu/")

	else:
		fm = Student_list()

	
	return render(request,'enroll/create1.html',{'form':fm})

def create_update(request,pk):
	if request.method == 'POST':
		stu =Student_list_table.objects.get(id=pk)
		fm = Student_list(request.POST,instance=stu)
		if fm.is_valid():
			fm.save()
			return redirect("/api/stu/")

	else:
		stu =Student_list_table.objects.get(id=pk)
		fm = Student_list(instance=stu)

	return render(request,'enroll/update1.html',{'form':fm})			

#################################################################


def home2(request):
	data = Student_mark_table.objects.all() 
	return render(request,'enroll/home2.html',{'data':data})


def create_mark(request):
	if request.method == "POST":
		fm = Student_mark(request.POST)
		if fm.is_valid():

			student = fm.cleaned_data['student']
			mark = fm.cleaned_data['marks']

			

			reg = Student_mark_table(student=student,marks=mark)
			reg.save()
			fm = Student_mark()
			return redirect("/api/stu1/")

	else:
		fm = Student_mark()

	
	return render(request,'enroll/create2.html',{'form':fm})

def mark_update(request,pk):
	if request.method == 'POST':
		stu =Student_mark_table.objects.get(id=pk)
		fm = Student_mark(request.POST,instance=stu)
		if fm.is_valid():
			fm.save()
			return redirect("/api/stu/")

	else:
		stu =Student_mark_table.objects.get(id=pk)
		fm = Student_mark(instance=stu)

	return render(request,'enroll/update2.html',{'form':fm})			
