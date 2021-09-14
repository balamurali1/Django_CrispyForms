from django import forms
from enroll import models

class StudentRegistration(forms.ModelForm):
	class Meta:
		model = models.User
		fields = ['name','email','password']
		labels ={'name':'Enter Name','email':'Enter Email','password':'Enter password'}
		widgets = {'password':forms.PasswordInput}