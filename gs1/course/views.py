from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#This video is gs_20 (create function Based view in django)

#HttpRespone anedi only variable,text,htmlformats code Excecute chesthundi..	


def Home_Page(request):    #request is the mandatory parameter,request anedi HttpRequest class Yooka Object
	return HttpResponse('This is Home Page')

def learn_django(request):
	return HttpResponse('Hello Django')   #HttpResponse it is the class 

def learn_html(request):
	return HttpResponse('<h1>Hell Geekyshows</h1>')

def learn_var(request):
	a = " Hi Geekyshows"
	return HttpResponse(a)

def learn_add(request):
	a = 10
	b = 15
	c = a+b
	return HttpResponse(c)

def learn_format(request):
	a = 10
	b = 12
	c = a*b
	d = 'Hello Geekyshows!!how are you'
	return HttpResponse(f'c value is:{c}'+','+f'D text is:{d}')


				