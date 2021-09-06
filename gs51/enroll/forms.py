from django import forms

class StudentRegistration(forms.Form):
	name = forms.CharField(label="You Name",label_suffix='-',initial='Murali',
		required=False,help_text="Limit 70 char",disabled=True)
	email = forms.EmailField()
	mobile = forms.IntegerField()
	key = forms.CharField(widget=forms.HiddenInput())