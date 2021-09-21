from django.shortcuts import render
from datetime import datetime

# Create your views here.

def learn_django(request):

	########## variable Filter #############
	'''
	django_details = {'nm':'Django is Awesome','fm':False,'ch':'GEEKYSHOWS'}
	return render(request,'enroll/courseone.html',context = django_details)
	'''
	#(OR)

	'''
	django_details = {'nm':'Django is Awesome','fm':False,'ch':'GEEKYSHOWS'}
	return render(request,'enroll/courseone.html',django_details)
	'''
	#(OR)
	'''
	return render(request,'enroll/courseone.html',{'nm':'django is Awesome',
		'fm':False,'ch':'GEEKYSHOWS'})
	'''


	############ datetime #################
	'''
	d = datetime.now()
	return render(request,'enroll/courseone.html',{'dt':d})
	'''
	

	############## floatformat ##############

	return render(request,'enroll/courseone.html',{'p1':56.24321,'p2':56.000,'p3':56.37000})

	
	