from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Single Application with multiple Functions.

def Home_Page(request):
	return HttpResponse('This is Home Page')

def learn_django(request):
	return HttpResponse('Hello Django')

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

def var(request):
	a = '<h1>Hello variable</h1>'
	return HttpResponse(a)	