from django import forms
from django.core import validators

#ela

def starts_with_m(value):
	if value[0] != 'M':
		raise forms.ValidationError('Name should start with M')

def starts_with_s(value):
	if value[0] != 's':
		raise forms.ValidationError('City should start with s')

def starts_with_k(value):
	if value[0] != 'K':
		raise forms.ValidationError('Email should start with K')


class Student(forms.Form):
	name = forms.CharField(validators = [starts_with_m])
	city = forms.CharField(validators = [starts_with_s])
	email = forms.EmailField(validators = [starts_with_k])
