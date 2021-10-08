from django.shortcuts import render
from enroll.models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

class StudentDetailView(DetailView):
	model = Student
	template_name = 'enroll/student.html'


class StudentListView(ListView):
	model = Student