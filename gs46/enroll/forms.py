from django import forms

class StudentRegistration(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	age = forms.IntegerField()
	city = forms.CharField()
	village = forms.CharField()
	phone = forms.IntegerField()
	

