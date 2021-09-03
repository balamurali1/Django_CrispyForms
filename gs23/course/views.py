from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
	return HttpResponse('Hello Geekyshows')

def learn_java(request):
	return HttpResponse('Hello Java How are you')	
	