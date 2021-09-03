from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def django_learn(request):
	return HttpResponse('Geekyshows Django')