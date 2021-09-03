from django import forms

STATES = (
    ('', '---Selete State---'),
    ('Ap', 'AndhraPradesh'),
    ('TS', 'Telangana'),
    ('CH', 'Chennai'),
    ('DL','Delhi'),
    ('KA','karnataka')

)

DISTRICT=(
	('','---Choose Dist---'),
	('KL','Kurnool'),
	('AT','Anantapuram'),
	('kA','Kadapa'),
	('CHI','Chittoor')

	)

class AddressFrom(forms.Form):
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	address_1 = forms.CharField(label='Address',widget=forms.Textarea(attrs={'rows':3,'placeholder':'H.No:1234 Main st'}))
	address_2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'placeholder':'Apartment,studio,or floor'}))
	city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City Name'}))
	district = forms.ChoiceField(choices=DISTRICT)
	state = forms.ChoiceField(choices=STATES)
	zip_code = forms.CharField(label='Zip')
	check_me_out = forms.BooleanField(required=False)