from django import forms

class StudentRegistration(forms.Form):
	name = forms.CharField(label='1.YourName',error_messages={'required':'(Enter valid Name)'})
	email = forms.EmailField(label='2.YourEmail',error_messages={'required':'(Enter valid email)'},min_length=5,max_length=50)
	password=forms.CharField(label='3.YourPassword',min_length=5,max_length=50,
		widget=forms.PasswordInput,error_messages={'required':'(Enter Your valid Password)'})