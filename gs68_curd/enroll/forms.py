from django import forms
from enroll.models import User

class StudentRegistration(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name','email','password']
		widgets = {

		'password':forms.PasswordInput(render_value = True )
		 }
