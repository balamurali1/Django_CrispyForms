from django.shortcuts import render
from enroll.models import Student
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from enroll.forms import StudentForm
'''
from django import forms



class StudentCreateView(CreateView):
	model = Student
	fields = ['name','email','password']
	#success_url = '/create/'  #ikkada url name echanu okay na..adhey url lo ki vasthundi...
	success_url = '/thanks/'

	def get_form(self):
		form = super().get_form()
		form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
		form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
		return form
'''
		#(OR)


class StudentCreateView(CreateView):
	form_class = StudentForm
	template_name = 'enroll/student_form.html'
	success_url = '/thanks/'	


class ThanksTemplateView(TemplateView):
	template_name = 'enroll/thanks.html'	

