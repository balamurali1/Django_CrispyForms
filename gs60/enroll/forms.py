from django import forms

class Student(forms.Form): #idigo ikkada Form is super()
	name = forms.CharField()
	email =forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)


	# def clean(self):
	# 	cleaned_data=super().clean()  #ee line lekunte kuda rayavachunu,#super() ante Form(parent ani) ani artham,ee Form lo ne "clean()" method untundi..


	# 	valname = self.cleaned_data['name']
	# 	if len(valname) < 4:
	# 		raise forms.ValidationError('Name should be more than or equal 4 char')

	# 	valemail = self.cleaned_data['email']	
	# 	if len(valemail) < 10:
	# 		raise forms.ValidationError('Email should be more than or equal 10 char')	

	# 	valpass = self.cleaned_data['password']
	# 	if len(valpass) < 5:
	# 		raise forms.ValidationError('Password should be more than 5 with Special char,Numeric Char')

					#(OR)



	def clean(self):
		cleaned_data=super().clean()  #ee line lekunte kuda rayavachunu,#super() ante Form(parent ani) ani artham,ee Form lo ne "clean()" method untundi..

		valname = self.cleaned_data['name']
		valemail = self.cleaned_data['email']
		valpass = self.cleaned_data['password']

		if len(valname) < 4:
			raise forms.ValidationError('Name should be more than or equal 4 char')

			
		if len(valemail) < 10:
			raise forms.ValidationError('Email should be more than or equal 10 char')	

		
		if len(valpass) < 5:
			raise forms.ValidationError('Password should be more than 5 with Special char,Numeric Char')	



