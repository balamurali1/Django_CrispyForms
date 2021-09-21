from django.shortcuts import render

# Create your views here.

def learn_django(request):

	#forloop data dictionary
	data = {'stu1':{'name':'Rahul','roll':101},
			'stu2':{'name':'Sonam','roll':102},
			'stu3':{'name':'Raj','roll':103},
			'stu4':{'name':'Anu','roll':104},
	}	
	return render(request,'enroll/courseone.html',{'data':data})



	'''
	#forloop key,value
	data = {'name':'Rahul','roll':101}
	return render(request,'enroll/courseone.html',{'data':data})
	'''


	# dictionary
	'''
	stu = {'stu1':{'name':'Rahul','roll':101},
			'stu2':{'name':'Sonam','roll':102},
			'stu3':{'name':'Raj','roll':103},
			'stu4':{'name':'Anu','roll':104},
	}

	students = {'student':stu}
	return render(request,'enroll/courseone.html',students)
	'''



	'''
	#forloop.conter
	student = {'names':['Rahul','Sonam','Raj','Anus']}
	return render(request,'enroll/courseone.html',student)
	'''
	'''
	#forloop.first
	student = {'names':['Rahul','Sonam','Raj','Anus']}
	return render(request,'enroll/courseone.html',student)
	'''
	'''
	#forloop.last
	student = {'names':['Rahul','Sonam','Raj','Anus']}
	return render(request,'enroll/courseone.html',student)
	'''

	'''
	#forloop.revcounter
	student = {'names':['Rahul','Sonam','Raj','Anus']}
	return render(request,'enroll/courseone.html',student)
	'''
	
	'''
	#for,empty
	student = {'names':['Rahul','Sonam','Raj','Anus']}
	return render(request,'enroll/courseone.html')#ikkada student ni call cheyaku appudu {% empty %} lo unnadi kanipisthadi..
	'''


	'''
	#for loop
	student = {'names':['Rahul','Sonam','Raj','Anus']}
	return render(request,'enroll/courseone.html',student)
	'''


	'''
	#if,elif,else,==
	#return render(request,'enroll/courseone.html',{'nm':'Django'})
	#return render(request,'enroll/courseone.html',{'st':5})
	#return render(request,'enroll/courseone.html')
	'''

	'''
	#if,elif,else
	#return render(request,'enroll/courseone.html',{'nm':'Django'})

	#return render(request,'enroll/courseone.html',{'st':5})	

	#return render(request,'enroll/courseone.html',{'nm':'','st':''})	
	'''

	'''
	#if,else, ==
	#return render(request,'enroll/courseone.html',{'nm':'Django'})

	#return render(request,'enroll/courseone.html',{'nm':'tjango'})
	'''
	
	'''
	#if else condition
	#return render(request,'enroll/courseone.html',{'nm':'Django'}) #idi True kada
	
	#return render(request,'enroll/courseone.html',{'nm':''}) #idi False kada
	'''

	'''
	#length filter
	return render(request,'enroll/courseone.html',{'nm':'Django'})
	'''

	'''
	# not,==
	return render(request,'enroll/courseone.html',{'nm':'Django','st':5})
	'''

	#return render(request,'enroll/courseone.html',{'nm':True})
			#(OR)	
	#return render(request,'enroll/courseone.html',{'nm':'Mrali'})
			#(OR)
	#return render(request,'enroll/courseone.html',{'nm':False})

	'''

	#and operator
	return render(request,'enroll/courseone.html',{'nm':'Dajngo','st':5})
	'''
	'''
	#or operator
	return render(request,'enroll/courseone.html',{'nm':'Dajngo'})
	'''

	'''
	#not operator
	return render(request,'enroll/courseone.html',{'nm':'Dajngo'})	
	'''
	
	'''
	#== operator	
	return render(request,'enroll/courseone.html',{'nm':'Django'})
	'''
	
	'''		
	# == ,and
	return render(request,'enroll/courseone.html',{'nm':'Django','st':5})
  	'''
	'''	
  	# ==,or
	return render(request,'enroll/courseone.html',{'nm':'Django','st':5})
	'''  	

  	
  

