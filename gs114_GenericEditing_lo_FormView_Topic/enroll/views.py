from django.shortcuts import render,HttpResponse
from enroll.forms import ContactForm,FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

# Create your views here.

#####################################
class ContactFormView(FormView):
	template_name = 'enroll/contact.html'
	form_class = ContactForm
	success_url = '/thankyou/'
	initial = {'name':'Murali'}
	def form_valid(self,form):
		print(form)
		print(form.cleaned_data['name'])
		print(form.cleaned_data['email'])
		print(form.cleaned_data['msg'])

		return super().form_valid(form)
		
		#return HttpResponse('Msg Sent')


class ThanksTemplateView(TemplateView):
		template_name = 'enroll/thankyou.html'
##########################################

class FeedbackFormView(FormView):
	template_name = 'enroll/contact1.html'
	form_class = FeedbackForm
	success_url = '/thankyou1/'

class FeedbackTemplateView(TemplateView):
		template_name = 'enroll/thankyou1.html'









