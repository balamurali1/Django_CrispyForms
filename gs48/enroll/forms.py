from django import forms

class StudentRegistration(forms.Form):
	name = forms.CharField(required=False)  #U can see viewpage Source(ctrl+u)
	email = forms.EmailField(required=True)
	last_name = forms.CharField(required=False)

	
