from django.shortcuts import render

# Create your views here.

		# Variable{{}} Topic in DTL 
'''
def learn_django(request):
	return render(request,'course/courseone.html',context={'nm':'Django'})
'''

def learn_django(request):
	cname = 'Django'
	duration = '4 Months'	
	seats = 10
	django_details = {'nm':cname,'du':duration,'st':seats}

	return render(request,'course/courseone.html',context=django_details)