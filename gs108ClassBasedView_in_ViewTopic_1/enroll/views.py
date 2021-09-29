from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

'''
This is Parent class 
'''
class MyView(View):
	name = 'Sonam' #class variable 
	def get(self,request): #self,request parametrs okay
		return HttpResponse(self.name) #ela parameter tho call chesha nu.

#Class variable ni class 'method lo' unde parameter tho call cheyavachunu.


'''
This is Chaild class,parent lo unde attributes ani ekadaku vasthai...
'''
class MyViewChaild(MyView): #ikkada Inheriate cheshanu parent ni chaild lo ki
	def get(self,request):
		return HttpResponse(self.name)		