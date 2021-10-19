from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView,PasswordChangeDoneView
from  myapp.forms import LoginForm

# Create your views here.
 
'''
Note: urls.py lo unde urls ni ela nituga views.py lo rasukovachunu...,urls.py lo kuda rayavahunu
akkada rasthe confusion ga unte ele views.py rasi urls.py lo import cheyavachunu..

urls.py lo anni urls okay dagara rashamu adi gs122_Customize_Authentication
'''

class MyLoginView(LoginView):
 	template_name='myapp/login.html'  #custome templates evi okay na...
 	authentication_form=LoginForm


class MyLogoutView(LogoutView):
 	template_name='myapp/logout.html'  #custome templates evi okay na...
 

class MyPasswordChangeView(PasswordChangeView):
 	template_name='myapp/changepass.html'  #custome templates evi okay na...
 	success_url='/changepassworddone/'


class MyPasswordChangeDoneView(PasswordChangeDoneView):
 	template_name='myapp/changepassdone.html'  #custome templates evi okay na...
 	


