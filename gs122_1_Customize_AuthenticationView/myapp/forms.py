from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _




class LoginForm(AuthenticationForm):
	username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'myuser'}))
	password = forms.CharField(
		label=_("Password"),
		strip = False,
		widget = forms.PasswordInput(attrs={'autocomplete':'current-password','class':'mypass'}))

'''
Note: CSS apply cheyali ante,by default ga django code lo 'class' attribute undadu okay na..
kabbati css apply cheyadaniki first forms.py create chesi tharuvatha field create chesi
haa tharuvatha haa filed lo class attribute ni mention cheyali.tharuvatha,class attribute attach aindo ledo thelusukovali ante"browser lo control view" chusukovali
forms.py lo unde 'LoginForm' ni login urls ki attach cheyali okay na..
'''	