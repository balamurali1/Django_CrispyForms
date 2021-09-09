from django import forms
from enroll import models
#from enroll.models import User

class StudentRegistration(forms.ModelForm):
	class Meta:
		model = models.User
		#model = User
		fields = ['name','email','password']
		widgets = {'password':forms.PasswordInput}