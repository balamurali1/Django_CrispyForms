from django.shortcuts import render
from enroll.models import Student
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

# Create your views here.

class StudentCreateView(CreateView):
	model = Student
	fields = ['name','email','password']
	'''
	Note: form create kvali ante forms.py lo rasi manamu form create chesthamu kada..appudud danini
	html file lo rasi chupisthamu kada..
	ala kakunda only simple ga models.py lo  
	attributes ni views.py ela echi rayavachunu  fields =['name','email','password']
	ee attributes tho ne 'form'  create auvthundi, malli database lo table kuda create auvthundi.
	'''
	
	'''
	ee class lo template_name anedi yenduku rayaledu ante by default
	 ga django student_form.html ani thisukuntundi. ee file anedi template floder lo undi chudu
	 ikkada rayaka poina kuda pani chesthundi..
	'''


	#success_url = '/create/'  #ikkada url name echanu okay na..adhey url lo ki vasthundi...
	success_url = '/thanks/'

class ThanksTemplateView(TemplateView):
	template_name = 'enroll/thanks.html'	

