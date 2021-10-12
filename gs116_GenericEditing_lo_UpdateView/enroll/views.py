from django.shortcuts import render
from enroll.models import Student
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.base import TemplateView

# Create your views here.

class StudentCreateView(CreateView):
	model = Student
	fields = ['name','email','password']
	success_url = '/thanks/' #ee url lo ki ravali ani artham..

class ThanksTemplateView(TemplateView):	
	template_name = 'enroll/thanks.html'



class StudentUpdateView(UpdateView):
	model = Student
	fields = ['name','email','password']
	success_url = '/updatethanks/'

class ThanksUpdateTemplateView(TemplateView):	
	template_name = 'enroll/thanksupdate.html'
