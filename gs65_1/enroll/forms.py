from django import forms
from enroll import models

class StudentRegistration(forms.ModelForm):

	# class Meta:
	# 	model = models.User
	# 	fields = ['name','email','password']
	# 	labels = {'name':'Enter Name','email':'Enter Email','password':'Enter Password'}
	# 	widgets = {'password':forms.PasswordInput} 

		#(OR)

	#models.py lo unde fields change cheyali ante forms.py lo ikkada change cheyavachunu.nenu Ex ga 'name' thisukoni andulo (**kwargs) change chesha..
	name = forms.CharField(max_length=50,required=False)
	
	class Meta:
		model = models.User
		fields = ['name','email','password']
		labels = {'name':'Enter Name','email':'Enter Email','password':'Enter Password'}
		widgets = {'password':forms.PasswordInput} 