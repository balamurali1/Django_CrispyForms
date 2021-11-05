from django.contrib.auth.models import User #built-in class in python(vitini django ne rasi unchindi.. )
from django.contrib.auth.forms import UserCreationForm,UserChangeForm #built-in class in python
from django import forms

#Note: so manamu ikkada ee rendu Built-in classes ni okadanitho marokatini 'Override' chesthunnamu..


class SignUpForm(UserCreationForm):
	password2 = forms.CharField(label='Confirm Password(Again)',widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email'] 

		labels = {'email':'Email'} #fields ni override cheyadam..
# ikkada 'User' ante data base lo by default ga unna table ani artham..
#fields ni labels ani kuda antaru..


class EditUserProfileForm(UserChangeForm):
	password = None
	class Meta:
		model=User
		fields=['username','first_name','last_name','email','date_joined','last_login']
		labels = {'email':'Email'}


class EditAdminForm(UserChangeForm):
	password = None
	class Meta:
		model=User
		fields="__all__"
		labels = {'email':'Email'}		
