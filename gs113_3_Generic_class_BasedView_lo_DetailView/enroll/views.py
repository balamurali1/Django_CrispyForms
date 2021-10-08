from django.shortcuts import render
from enroll.models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

class StudentDetailView(DetailView):
	model = Student
	template_name = 'enroll/student.html'


	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		context['all'] = self.model.objects.all().order_by('name')
		return context


'''
Note:context['all'] indulo yedaina name pettukovachunu...niestham,nenu
'all' ani pettina...
'''


class StudentListView(ListView):
	model = Student