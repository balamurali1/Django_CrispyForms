from django.shortcuts import render

# Create your views here.

#Note:Dynamic data is nothing but 'Python code'

#Model-1(vvvvvIMP)
def learn_django(request):
	coursename = {'cname':'Django','fees':300,'city':'HYD'} #Dynamic Data This one
	return render(request,'course/one.html',context=coursename)

#Model-2
def learn_python(request):
	person_Details = {'name':'Balamurali','age':25,'color':'Black'}
	return render(request,'course/two.html',person_Details)	

#Model - 3
def learn_java(request):
	return render(request,'course/three.html',{'city':'Nandikotkur','town':'Kurnool'})	

#Model-4
def learn_php(request):
	cname = 'Murali'
	age = 25
	color = 'Black'
	village = 'Nandikotkur'
	town = 'Kurnool'
	state = 'Ap'

	data = {'nm':cname,'a':age,'c':color,'v':village,'t':town,'s':state}
	
	return render(request,'course/four.html',data)	