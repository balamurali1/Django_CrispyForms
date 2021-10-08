from django.shortcuts import render
from enroll.models import Student
from django.views.generic.list import ListView

# Create your views here.

class StudentListView(ListView):
	model = Student
	template_name_suffix = '_get' 
	#ordering = ['name']
	ordering = ['roll']

'''
template_name_suffix==>idi template lo ni html file yooka old name ni 
modification chesthundi..ela pettina tharuvatha manamu mana hands tho file
name change cheyali

EX:
student_list(default).html unna danini manamu  template_name_suffix  use chesi
appudu student_get ani petinamu kada.

ikkada observe cheai okati adi vachesi html file name change cheshamu kada...
kani haa html file lo ni "{% for stu in student_list %}" indu lo unde
"student_list(default)" name ni change cheyavalasina auvsaram ledu...
internal ga student_list matrame run auvthundi....

'''