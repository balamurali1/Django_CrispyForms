from django.urls import path,register_converter
from api import views, converters

register_converter(converters.FourDigitYearConverter,'yyyy') #yyyy(custom path) palce lo yedaina rasuko kani,4 digits matrame undali

urlpatterns = [
	path('session/<yyyy:year>/',views.show_details,name='subdetail'),
]