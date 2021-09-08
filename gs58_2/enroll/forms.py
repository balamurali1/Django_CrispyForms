from django import forms

class StudentRegistration(forms.Form):
	#CharField()
	name = forms.CharField(min_length=5,max_length=10,error_messages={'required':'Enter Your Name'})

	#IntegerField()
	roll = forms.IntegerField(error_messages={'required':'Enter Your Roll Number'})

	#DecimalField()
	price = forms.DecimalField(min_value=5,max_value=40,max_digits=4,decimal_places=2)


	#FloatField()
	rate = forms.FloatField(min_value = 5,max_value = 40)

	#SlugField()
	comment = forms.SlugField()

	#EmailFiled()
	email = forms.EmailField(min_length = 5,max_length = 50)

	#URLField()
	website = forms.URLField(min_length = 5,max_length = 50)

	#CharFiled()
	password = forms.CharField(min_length = 5,max_length = 50,widget = forms.PasswordInput)

	description = forms.CharField(widget = forms.Textarea)

	feedback = forms.CharField(min_length = 5,max_length = 50,
		widget = forms.TextInput(attrs = {'class':'somecss1 somecss2',
			'id':'uniqueid'}))
	notes = forms.CharField(widget = forms.Textarea(attrs = {'row':3,'cols':50}))		 

	#BooleanField()
	#agree = forms.BooleanField()
	#agree = forms.BooleanField(label = 'I Agree')
	agree = forms.BooleanField(label_suffix = '',label = 'I Agree')
	#agree = forms.BooleanField(label_suffix = '',label = 'I Agree',error_messages = {'required':'Are You Agree'})
