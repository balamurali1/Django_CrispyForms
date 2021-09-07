from django import forms
import re

class StudentRegistration(forms.Form):
	name = forms.CharField()
	email=forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

#Syntax:
	#  def clean_<fieldname>()

	def clean_name(self):
		valname = self.cleaned_data.get('name') #valname = self.cleaned_data['name']
		if len(valname) < 4:
			raise forms.ValidationError('Enter more than or equal 4 char')
		return valname

	def clean_email(self):
		valemail = self.cleaned_data.get('email')
		if len(valemail) < 10:
			raise forms.ValidationError('Enter should be more than or equal 10 char')
		return valemail	

	def clean_password(self):
		valpass = self.cleaned_data['password']
		if len(valpass) < 4:
			raise forms.ValidationError('Enter more then 4 chat with special Char[@#&%],Numeric char[123456..]')
		return valpass		
