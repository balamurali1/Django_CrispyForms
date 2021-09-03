from django import forms

class StudentRegistration(forms.Form):
	name = forms.CharField(help_text='(Your Name)')
	email = forms.EmailField(help_text='(Your Email)')
	first_name = forms.CharField(help_text='(Your First_Name)')
