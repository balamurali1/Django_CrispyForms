from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Single View function with Multiple URL's
def learn_django(request):
	return HttpResponse('Hello Django Murali')