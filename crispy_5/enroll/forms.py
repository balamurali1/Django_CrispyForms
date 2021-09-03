from django import forms
from django.core import validators

#2) diniki str is not callble ani error vasthundi...
def check_size(value):
	if len(value) < 6:
		raise forms.ValidationError('The Password is too short')



class AddressFrom(forms.Form):
	first_name = forms.CharField(initial = 'First Name',)
	last_name = forms.CharField(required=False)
	email = forms.EmailField(help_text = 'write your email', required=False)
	Address = forms.CharField(required = False, )
	Technology = forms.CharField(initial = 'Django,Python,Java', disabled = True)
	age = forms.IntegerField(required = False, )

# 1)i am using here only MinLengthValidator	direct ga...!!	
	#password = forms.CharField(widget = forms.PasswordInput, validators = [validators.MinLengthValidator(6)])

# 2) Check_size	
	password = forms.CharField(widget = forms.PasswordInput, validators = ['check_size'])

#3) validate for a perticular Field
	#password = forms.CharField(widget = forms.PasswordInput)
	
	re_password = forms.CharField(help_text='renter Your password',widget = forms.PasswordInput, required = False)
	botcatcher = forms.CharField(widget=forms.HiddenInput,required=False)


#3)
	# def clean_password(self):
	# 	password = self.cleaned_data['password']
	# 	if len(password) < 4:
	# 		raise forms.ValidationError('Password is too short')
	# 	return password	
