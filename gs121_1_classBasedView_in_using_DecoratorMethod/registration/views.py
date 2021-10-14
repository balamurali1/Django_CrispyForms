from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
'''
class ProfileTemplateView(TemplateView):
	template_name = 'registration/profile.html'

	@method_decorator(login_required)  #ela dinini 3 lines lo rayakunda single line lo rayavachunu...
	def dispatch(self,*args,**kwargs):
		return super().dispatch(*args,**kwargs)  #super() ante-->'ProfileTemplateView' ani artham


class AboutTemplateView(TemplateView):
	template_name = 'registration/about.html'

	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super().dispatch(*args,**kwargs)  #super() ante-->'AboutTemplateView' ani artham


class StaffTemplateView(TemplateView):
	template_name = 'registration/staff.html'

	@method_decorator(staff_member_required)
	def dispatch(self,*args,**kwargs):
		return super().dispatch(*args,**kwargs)  #super() ante-->'StaffTemplateView' ani artham

'''

'''
Note: admin.site lo staff dhagara 'Tick(True)',mark add chesthu remove chesthu,
try chesthu undali "StaffTemplateView" ni
'''
						#(OR)

@method_decorator(login_required,name='dispatch') #simple ga single line lo dinini rayavachunu...
class ProfileTemplateView(TemplateView):
	template_name = 'registration/profile.html'

	
@method_decorator(login_required,name='dispatch') 
class AboutTemplateView(TemplateView):
	template_name = 'registration/about.html'


@method_decorator(staff_member_required,name='dispatch') 
class StaffTemplateView(TemplateView):
	template_name = 'registration/staff.html'



'''
Note: admin.site lo staff dhagara 'Tick(True)',mark add chesthu remove chesthu,
try chesthu undali "StaffTemplateView" ni
'''
	



