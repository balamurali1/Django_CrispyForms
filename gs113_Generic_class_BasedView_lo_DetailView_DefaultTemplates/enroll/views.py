from django.shortcuts import render
from enroll.models import Student
from django.views.generic.detail import DetailView

# Create your views here.

class StudentDetailView(DetailView):
	model = Student



'''
Note:
Django pics  carefull ga observer cheai nikey artham auvthundi..
Default templates,Default Context..etc.	
'''