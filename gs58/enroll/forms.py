from django import forms

class ContactForm(forms.Form):
	title = forms.CharField(max_length=150)
	message = forms.CharField(max_length=200,widget=forms.TextInput)


class SubcriptionForm(forms.Form):
	email = forms.EmailField()
