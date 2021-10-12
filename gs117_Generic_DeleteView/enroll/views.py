from django.views.generic.edit import CreateView,UpdateView, DeleteView
from . models import Student
from django.views.generic.base import TemplateView
from . forms import StudentForm

# Create your views here.


class StudentCreateView(CreateView):
	form_class = StudentForm
	template_name = 'enroll/student_form.html'
	success_url = '/thanks/'


class StudentUpdateView(UpdateView):
	model = Student
	form_class = StudentForm
	template_name = 'enroll/student_form.html'
	success_url = '/thanksupdate/'

class StudentDeleteView(DeleteView):
	model =Student
	success_url = '/create/'
	

class ThanksTemplateView(TemplateView):
	template_name = 'enroll/thanks.html'

class ThanksUpdateTemplateView(TemplateView):
	template_name = 'enroll/thanksupdate.html'