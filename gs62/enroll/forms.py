from django import forms

class Student(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	rpassword = forms.CharField(label='Password(Again)',widget=forms.PasswordInput)

	def clean(self):
		cleaned_data=super().clean()
		valpass = self.cleaned_data['password']
		valrpass = self.cleaned_data['rpassword']
		if valpass != valrpass:
			raise forms.ValidationError('Password does not match,Please Enter valid password!!')