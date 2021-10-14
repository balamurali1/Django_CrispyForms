from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ProfileTemplateView(TemplateView):
	template_name = 'registration/profile.html'


class AboutTemplateView(TemplateView):
	template_name = 'registration/about.html'

class StaffTemplateView(TemplateView):
	template_name = 'registration/staff.html'



#Note: admin.site ni logout chesukuntu try chesthu undali..
