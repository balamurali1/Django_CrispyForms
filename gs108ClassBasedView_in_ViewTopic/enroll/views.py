from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

'''
This is Function Based view okay,
function based view lo by default ga get() method untundi internal ga
so  function based view anedi automatic ga get() method thisukuntundi.
'''
def myview(request): 
	return HttpResponse('<h4>Function Based View</h4>')


'''
This is Class Based View okay,
class Based view lo by default ga get() undadu internal ga,kabbati appudu
urls.py lo class name rasetappudu dani pakkana 'as_view()' ane method rasthamu..okay na!!
'''
class MyView(View):
	def get(self,request):
		return HttpResponse('<h4>Class Based View</h4>')	

class MyVar(View):
	name = 'Sonam' #class variable
	def get(self,request): #self,request is the parameters okay
		return HttpResponse(self.name) #ela parameter tho call chesha nu.

#Class variable ni class 'method lo' unde parameter tho call cheyavachunu.


class MyPriority(View):
	name = 'Rahul'
	def get(self,request):
		return HttpResponse(self.name)	

class MyEmpty(View):
	name = '' #name='', name anedi blank lo undi ani anukokandi '' single quotation lo kali ga unna adi kuda count lo ki vasthundi.
	def get(self,request):
		return HttpResponse(self.name)	
