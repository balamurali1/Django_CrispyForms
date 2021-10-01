from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView

# Create your views here.

'''
1.direct ga url ni url.py lo unna RedirectView.as_view() lo rayavachunu.

2. leka pothey views.py lo class lowpala url ni echi,haa class name ni urls.py lo euvvali.
'''

class GeekyshowsRedirectView(RedirectView):
	url='https://www.tutorialsteacher.com/typescript'


class AmazonRedirectView(RedirectView):
	url='/'


class GeekyRedirectView(RedirectView):
	#url='https://studygyaan.com'
	pattern_name='midpage'

	permanent = True	   #idi status code ni esthundi.301 0 ani....cmd lo 
	#query_string = False  #by default
	query_string = True    #url enter cheshaka "?jfkjsdjfjds" ela pettu okyana..Question mark first undali,next yedaina type chesuko.


	def get_redirect_url(self,*args,**kwargs):
		print(kwargs)
		kwargs['pk']=23 #idi by default ga undela pettukovachunu,url lo yedi echina edey print auvthundi browser lo,cmd lo aithey url echinadi print auvthundi
		return super().get_redirect_url(*args,**kwargs)


	


class ShowsRedirectView(RedirectView):
	url='https://www.interviewbit.com'		