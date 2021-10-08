from django.shortcuts import render
from enroll.models import Student
from django.views.generic.list import ListView

# Create your views here.

class StudentListView(ListView):
	model = Student
	template_name = 'enroll/student.html'
	context_object_name = 'data'

	"""
	Note: 1.ikkada observer cheai,actually ga app lo unde html file name(first create chesina template ni 'default' antaru,already ee tamplate ni create chesi manamu  code mootham rasintamu),okavella 
	default template name change cheyali anukunte appudud view.py lo echina
	template_name = 'enroll/student.html'(custom template) name veru veru ga unna code anedi pani chesthundi okay na..

	2.kani indulo" first preparence vachesi view.py lo unde template_name = 'enroll/student.html' (custom template) ki untundi..."
	"second preparence vachesi app lo unde templates lo ni 'vere'  html files ki untundi...."
###############################################
	Note:1. ledu nenu compalsary app lo unde template name change cheyali anukunte
	appudu app lo ni template name change chesetappudu 
	view.py lo unde (template_name = 'enroll/student.html') same name pettukovachunu..
	code work auvthundi.	

	kani internal ga matramu {% for stu in student_list %} html file lo student_list 
	anedi default ga run auvthundi..yendu kante code anedi starting lo haa html file lo ne
	rashamu kabbati...adi alane work auvthundi..

##########################################
	Note:
	ledu compalsary {% for stu in student_list %} student_list name change cheyali anukunte
	appudu" context_object_name" use cheyali.tharuvatha vachesi context_object_name
	yooka value ni {% for stu in student_list %} student_list place lo past cheyali
	appudu student_list(default) anedi work cheyadu..
	"""


