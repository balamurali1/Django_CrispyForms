from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class HomeTemplateView(TemplateView):     
	template_name = 'enroll/classtem.html'


class PageTemplateView(TemplateView):  #ikkada 'super()' vachesi PageTemplateView class okay na..
	template_name = 'enroll/page.html'	

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)

		'''
		context['name'] = 'Sonam'
		context['roll'] = 101
		'''
#(OR)		
		context = {'name':'Murali','roll':102} 

		return context

	

class ExTemplateView(TemplateView):  #ikkada 'super()' vachesi ExTemplateView class okay na..
	template_name = 'enroll/extra.html'	

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)

		'''
		Note:
		ela context ni dictionary lo esthe extra_context anedi work kadu...
		first dictionary context ni comment cheai, ela context ni list rupam lo rasthe extra_context panichesthundi.
		'''
		#context = {'name':'Murali','roll':102}  


		context['name'] = 'Sonam'
		context['roll'] = 101

		return context		



class KeyArgView(TemplateView):  #ikkada 'super()' vachesi KeyArgView class okay na..
	template_name = 'enroll/key.html'	

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs) 

		'''
		 **kwargs ante url lo ela euvvali like 
		 Ex:
		 <int:pk>,
		 <int:id>,
		 <int:roll>  #roll means 'key' ani artham vasthundi..
		'''

		context['name'] = 'Sonam'
		context['roll'] = 101

		print(context) # idi cmd lo print auvthundi...
		print(kwargs) 
		'''
		Ex: kwargs anedi cmd lo print yela auvthundi ante,<int:cls> cls  key
		ga thisukoni,brower url lo echina data ni 'value' ga thisukoni print auvthundi.
		ela dictionary ga {'cls':12} cmd lo.
		''' 
		return context