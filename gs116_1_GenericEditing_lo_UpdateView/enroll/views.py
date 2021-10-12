
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from . models import Student
from django.views.generic.base import TemplateView
from django import forms
from . forms import StudentForm

# Create your views here.
# class StudentCreateView(CreateView):
# 	model = Student
# 	fields = ['name','email','password']
# 	success_url = '/thanks/'

# 	def get_form(self):
# 		form = super().get_form()
# 		form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
# 		return form

# 	def get_form(self):
# 		form = super().get_form()
# 		form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'mypass'})
# 		return form	



# class StudentUpdateView(UpdateView):
# 	model = Student
# 	fields = ['name','email','password']
# 	success_url = '/thanksupdate/'

# 	def get_form(self):
# 		form = super().get_form()
# 		form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
# 		return form

# 	def get_form(self):
# 		form = super().get_form()
# 		form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'mypass'})
# 		return form

#(or)

class StudentCreateView(CreateView):
	form_class = StudentForm
	template_name = 'enroll/student_form.html' #Custom Template
	success_url = '/thanks/'


class StudentUpdateView(UpdateView):
	model = Student
	form_class = StudentForm
	template_name = 'enroll/student_form.html'  #Custom Template
	success_url = '/thanksupdate/'



class ThanksTemplateView(TemplateView):
	template_name = 'school/thanks.html'



class ThanksUpdateTemplateView(TemplateView):
	template_name = 'school/thanksupdate.html'
