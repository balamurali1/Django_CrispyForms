from django import forms
from enroll.models import User


class StudentRegistration(forms.ModelForm):
	class Meta:
		model = User
		#fields = ['name','email','password']
			#(OR)
		#fields ="__all__"
		exclude = ['name'] #(OR) exclude = ('name',)# tuple lo oka item unte comma pettali pakkana
