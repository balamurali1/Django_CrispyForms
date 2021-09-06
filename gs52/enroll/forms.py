from django import forms

class StudentRegistration(forms.Form):
	#name ki password set cheyadam
	name = forms.CharField(widget=forms.PasswordInput)

	#password field create cheyali ante,passwordField saparet ga ledu kabbati
	#appudu	charfield ne use chesi andulo widget ni apply cheyali..ela...
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

	text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'TextArea'}))
	sex = forms.CharField(widget = forms.CheckboxInput)
	Address = forms.CharField(widget = forms.Textarea(attrs = {'class': 'somecss1','id':'uniqueid',
		'placeholder':'Address Mention Here'}))

	