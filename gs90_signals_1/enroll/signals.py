from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver


#------user_logged_in--------

'''
def login_success(sender,request,user,**kwargs):
	print("-------------------------------")
	print("Logged-in Signal..Run Intro...")
	print("Sender:",sender)
	print("Request:",request)
	print("User:",user)
	print("User Password:",user.password)
	print(f'kwargs:{kwargs}')

user_logged_in.connect(login_success,sender = User) #This is "Manual Connect Route" process
#Note:signal-->connect method-->(reciver function--->User)
'''

'''
Note:
	Here:
	    user_logged_in= Dinini signal antaru
		connect() is the Method okay..
		login_success is the 'Receiver Function' ani artham,connect method ni login_success(Receiver Function) ki connect cheai ani aduguthunnamu.
		sender=euvaru send chesthunaru ante User ani artham

	dinini  yela check cheyali ante just migrate chesi,createsuperuser chesi admin site login auvthey cmd lo print kavali.	
'''		


		#(OR)


@receiver(user_logged_in,sender=User)   #This is Decorator @ process
def login_success(sender,request,user,**kwargs):
	print("-------------------------------")
	print("Logged-in Signal..Run Intro...")
	print("Sender:",sender)
	print("Request:",request)
	print("User:",user)
	print("User Password:",user.password)
	print(f'kwargs:{kwargs}')



'''
Note: @Decorator process lo internal ga "login_success function" anedi @receiver lo unde (user_logged_in)  lo ki pothundi. 
'''
#################################################



#-----------user_logged_out-------------
'''
def log_out(sender,request,user,**kwargs):
	print("-------------------------------")
	print("Logged-out Signal..Run outro...")
	print("Sender:",sender)
	print("Request:",request)
	print("User:",user)
	print(f'kwargs:{kwargs}')

user_logged_out.connect(log_out,sender = User) #This is "Manual Connect Route" process
'''

		#(OR)


@receiver(user_logged_out,sender=User)   #This is Decorator @ process
def log_out(sender,request,user,**kwargs):
	print("-------------------------------")
	print("Logged-in Signal..Run outro...")
	print("Sender:",sender)
	print("Request:",request)
	print("User:",user)
	print(f'kwargs:{kwargs}')		

####################################################

#--------------user_login_failed------------

'''
def login_failed(sender,credentials,request,**kwargs):
	print("-------------------------------")
	print("Login-failed Signal.....")
	print("Sender:",sender)
	print('Credentials:',credentials)
	print("Request:",request)
	print(f'kwargs:{kwargs}')

user_login_failed.connect(login_failed) #This is "Manual Connect Route" process
'''

		#(OR)

@receiver(user_login_failed)   #This is Decorator @ process
def login_failed(sender,credentials,request,**kwargs):
	print("-------------------------------")
	print("Login-failed Signal.....")
	print("Sender:",sender)
	print('Credentials:',credentials)
	print("Request:",request)
	print(f'kwargs:{kwargs}')


