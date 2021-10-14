from django.shortcuts import render


# Create your views here.

def profile(request):
	return render(request,'registration/profile.html')


'''
Note: accounts/ ee url ni maname createcheyali,ee url datina tharuvatha
login/,logout/,password_change/.....etc vitini django  lo  by default rasi 
pettinaru gurthupettuko..

accounts/ login/ [name='login']
accounts/ logout/ [name='logout']
accounts/ password_change/ [name='password_change']
accounts/ password_change/done/ [name='password_change_done']
accounts/ password_reset/ [name='password_reset']
accounts/ password_reset/done/ [name='password_reset_done']
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm'] #diniki matramu cmd lo link vasthadi danini copy chesi browser lo chudu..
accounts/ reset/done/ [name='password_reset_complete']
accounts/ profile/ [name='profile']
'''	