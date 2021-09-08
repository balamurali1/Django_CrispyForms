from django import forms
from django.core import validators

class Student(forms.Form):
	name = forms.CharField(validators=[validators.MaxLengthValidator(10,message="Give  at least 10 char below")])
	city = forms.CharField(validators=[validators.MinLengthValidator(5,message=None)])
	email = forms.EmailField(validators=[validators.EmailValidator(message="It is not Good email")])