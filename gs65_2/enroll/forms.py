from django import forms
from enroll import models

class StudentRegistration(forms.ModelForm):
	name = forms.CharField(max_length=50,required=False)#models.py unna fields lo unna(**kwargs,args) chenage cheyali ante forms.py change cheyavachunu

	class Meta:
		model = models.User
		fields = ['name','email','password']
		labels = {'name':'Enter Name',
				'email':'Enter Email',
				'password':'Enter Password'}
		widgets = {'password':forms.PasswordInput}
		
