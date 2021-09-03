from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit,Row,Column
from django.forms.widgets import NumberInput
import datetime


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

FAVORITE_COLORS_CHOICES=[
	('','---Choose Color---'),
	('blue','Blue'),
	('green','Green'),
	('black','Black'),
	('yellow','Yellow'),
	('ornage','Orange'),
	('white','White'),
]

class AddressFrom(forms.Form):
	email_address = forms.EmailField(help_text='(This not Mandatory Email Id)',required=False,label='1.Enter Email')
	email = forms.CharField(help_text='Write Your Email_Id',required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
	password = forms.CharField(help_text='Enter Your Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
	re_password = forms.CharField(help_text='Enter Your Re-Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter Re-Password'}))
	birth_date = forms.DateField(help_text='Mention your DOB',widget=NumberInput(attrs={'type':'date'}))
	address_1 = forms.CharField(label='Address',widget=forms.Textarea(attrs={'rows':3,'placeholder':'H.No:1234 Main st'}))
	address_2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'placeholder':'Apartment,studio,or floor'}))
	city = forms.CharField(help_text='(This is not Mandatory)',required=False,widget=forms.TextInput(attrs={'placeholder':'City Name'}))
	district = forms.ChoiceField(choices=DISTRICT)
	state = forms.ChoiceField(choices=STATES,label="State")
	zip_code = forms.CharField(required=False,label="Zip_code")
	check_me_out = forms.BooleanField(required=True,label='Terms & conditions Okay!!for you click it.')
	day = forms.DateField(initial=datetime.date.today,help_text='Write Your day')
	favorite_colors = forms.MultipleChoiceField(help_text='Please Select Mul-Colors',required=False,choices=FAVORITE_COLORS_CHOICES)	


	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('email_address',css_class='form-group col-md-6 mb-0'),
				Column('email',css_class='form-group col-md-6 mb-0'),
				Column('password',css_class='form-group col-md-6 mb-0'),
				Column('re_password',css_class='form-group col-md-6 mb-0'),
				Column('birth_date',css_class='form-group col-md-6 mb-0'),
				Column('day',css_class='form-group col-md-6 mb-0'),
				Column('favorite_colors',css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
				),
			'address_1',
			'address_2',
			Row(
				Column('city',css_class='form-group col-md-4 mb-0'),
				Column('district',css_class='form-group col-md-3 mb-0'),
				Column('state',css_class='form-group col-md-3 mb-0'),
				Column('zip_code',css_class='form-group col-md-2 mb-0'),
				css_class='form-row'
				),
			'check_me_out',
			Submit('submit','Sign in')

			)