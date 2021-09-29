from django.shortcuts import render
from django.views import View
from enroll.forms import ContactForm
from django.http import HttpResponse

# Create your views here.

###################### Template process ################

def homefun(request): #This is Function based view.indulo get anedi by default ga untundi.
	return render(request,'enroll/home.html')


'''
#class Based view lo by default ga "get method undadu" kabbati get method thisukoni
self,request parameters maname euvvali.
'''
class HomeClassView(View): 
	def get(self,request):
		return render(request,'enroll/class.html')

################### context procee ##################################		

def about(request): #function Based context
	context = {'msg':'Welcome to Python & Django developers'}
	return render(request,'enroll/about.html',context = context)

class AboutClassView(View): #class Based context
	def get(self,request):
		context = {'msg':'Welcome to class Based Python and django developers'}
		return render(request,'enroll/aboutclass.html',context)


################### Forms ############################		

def contactfun(request): #Function based Form
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data['name']) #cleaned_data means get ani artham

			return HttpResponse('Thanks You are filling  function based form,form is submitted!!')

	else:
		form = ContactForm()

	return render(request,'enroll/contact.html',{'form':form})				
			


class ConntactFormView(View): #Class Based Form
	def get(self,request):  #form ni fill cheyakunda submit kodithey,getmethod dwara vachi ee code execute auvthundi
		form = ContactForm()
		return render(request,'enroll/contactclass.html',{'form':form})



	def post(self,request): #form ni fill chesi submit codithey,post method dwara vachi  ee code execute auvthundi..
		form = ContactForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data['name'])
			return HttpResponse('Thanks your Filling ClassBased Form,Form is Submited')




####################################################
	#Function Based Views process
'''
def newsfun(request):
	context = {'info':'CBI Enquery Why Geekyshows earns less Money'}
	return render(request,'enroll/new.html',context)
'''
	#(OR)

''''
def newsfun(request):
	template_name='enroll/new.html'
	context = {'info':'CBI Enquery Why Geekyshows earns less Money'}
	return render(request,template_name,context)	
'''

#(OR)

#Oka view function ki, urls.py lo multiple urls ni create chesi chupinchavachunu.
def newsfun(request,template_name):
	a=template_name
	context = {'info':'CBI Enquery Why Geekyshows earns less Money'}
	return render(request,a,context)	


		#class Based View Process

'''
class NewClassView(View): ##process-1 url ki
	def get(self,request):
		context = {'info':'CBI Enquery Why Geekyshows earns less Money'}
		return render(request,'enroll/newclass.html',context=context)		
'''

#(OR)

'''
class NewClassView(View):  #process-1 url ki
	def get(self,request):
		template_name = 'enroll/newclass.html'
		context = {'info':'CBI Enquery Why Geekyshows earns less Money'}
		return render(request,template_name ,context=context)				
'''

#(OR)

'''
class NewClassView(View):  #process-1 url ki
	template_name = 'enroll/newclass.html' #This is class variable idi method lo rayali ante self.variable_name
	def get(self,request):
		context = {'info':'CBI Enquery Why Geekyshows earns less Money'}
		return render(request,self.template_name,context=context)						

'''

'''
class NewClassView(View):   #process-2 url ki
	template_name = ''  
	def get(self,request):
		context = {'info':'CBI Enquery Why Geekyshows earns less Money'}
		return render(request,self.template_name,context=context)						

'''

class NewClassView(View):   #process-3 url ki
	template_name = ''  
	def get(self,request):
		context = {'info':'CBI Enquery Why Geekyshows earns less Money'}
		return render(request,self.template_name,context=context)						

#Note:Single class Based view ki multiple Urls create cheyadam...
