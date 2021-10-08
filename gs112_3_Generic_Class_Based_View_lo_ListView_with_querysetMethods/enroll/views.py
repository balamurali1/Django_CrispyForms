from django.shortcuts import render
from enroll.models import Student
from django.views.generic.list import ListView

# Create your views here.

class StudentListView(ListView):
	model = Student
	template_name = 'enroll/student.html'
	context_object_name = 'data'

	################## filter(),get_queryset() #########
	def get_queryset(self):
		return Student.objects.filter(course='Python')


#get_context_data() this return context data for displaying the list of objects(records)
	
	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		context['freshers'] = Student.objects.all().order_by('name')
		return context
'''
ikkada **kwargs anedi dictionary rupam lo esthundi kabbati, so 'freshers' anedi own ga key la ga thisukoni danini html file 
variable ga echamu..
	
'''

############## EX:cookies #######################

    def get_template_names(self):
		if self.request.COOKIES['user'] == 'murali':
			template_name = 'enroll/cookies.html'
		else:
			template_name = self.template_name #ikkada self.template_name lo template_name vachesi idi (template_name = 'enroll/student.html')starting lo undi chudu.idi run auvthundi else lo
		return template_name

'''
Dynamic templates evi (ante oka template run kakunte maroka template run auvthundi
ee process ni manamu if,else conditions use chesi rashamu...okay)
'''		

################## EX:admin.site ##################
	def get_template_names(self):
		if self.request.user.is_superuser:
			template_name = 'enroll/superuser.html'
		elif self.request.user.is_staff:
			template_name = 'enroll/staff.html'
		else:
			template_name = self.template_name
		return template_name
'''
ee code vachesi admin.site lo unde user tabale ni checkbox lo unde superuser,
staff, tick mark adharanga rashamu...
'''								