from django.shortcuts import render
from enroll.models import Student
from django.views.generic.detail import DetailView

# Create your views here.

class StudentDetailView(DetailView):
	model = Student
	template_name = 'enroll/student.html' #custom templates maname own ga create chesukovadam,django eninadi use cheyakunda maname create cheyadam
	context_object_name = 'stu' #custom  context maname create cheyadam.
	pk_url_kwarg = 'id' #urls.py lo chudu dini gurinchi...
