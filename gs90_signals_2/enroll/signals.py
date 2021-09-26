from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete,pre_migrate,post_migrate

from django.core.signals import request_started,request_finished,got_request_exception

from django.db.backends.signals import connection_created

#------user_logged_in--------

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
sender = User,ikkada User anedi  class okay na... user table by default ga untundi kabbati create cheyavalasina auvsaram ledu model.py lo.
kavali anukunte new tables ni models.py lo create chesukoo sender= xxx, ikkada echukoo.
'''

'''
Note: @Decorator process lo internal ga "login_success function" anedi @receiver lo unde (user_logged_in)  lo ki pothundi. 
'''
#################################################



#-----------user_logged_out-------------

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

@receiver(user_login_failed)   #This is Decorator @ process
def login_failed(sender,credentials,request,**kwargs):
	print("-------------------------------")
	print("Login-failed Signal.....")
	print("Sender:",sender)
	print('Credentials:',credentials)
	print("Request:",request)
	print(f'kwargs:{kwargs}')
#########################################################

########Bulit-in Objects(ante python by default ga esthundi) evi okay #######


			#-------pre_save-----

'''
Ex:Admin site lo ki loggin auvvagane ventane pre_save,post_save,user_logged_in
first work auvthai,built-in signals program lo 'user signal' tho pattu Built-in signals untene work auvthai..
lekunte only 'User signals'matrame panichesthi..

Ikkada Bulit-in methods unai kabbati work auvthunai..
'''

'''
New record create cheste if condition panichesthuni,
old record ni update chesthe else panichestundi.	

final ga save button meeda click chesthe pre_save,post_save signal panichesthai...
'''	


@receiver(pre_save,sender=User) #This is @Decorator process
def at_beginning_save(sender, instance, **kwargs): 
	print("-------------------------------")
	print("Pre Save Signal.....")
	print("Sender:",sender)
	print('Instance:',instance)
	print(f'kwargs:{kwargs}')
#pre_save.connect(at_beginning_save,sender=User) #This is "Manual Connect Route" process	


		#----post_save----


@receiver(post_save,sender=User) #This is @Decorator process
def at_ending_save(sender, instance, created, **kwargs): 
	if created:
		print("-----------created New record--------------------")
		print("Post Save Signal.....")
		print('New Record')
		print("Sender:",sender)
		print('Instance:',instance)
		print('Created:',created)
		print(f'kwargs:{kwargs}')
	else:
		print("----------Update old record--------------------")
		print("Post Save Signal.....")
		print('Update Record')
		print("Sender:",sender)
		print('Instance:',instance)
		print('Created:',created)
		print(f'kwargs:{kwargs}')
			
#post_save.connect(at_ending_save,sender=User) #This is "Manual Connect Route" process	

################################################################	

		#-------pre_delete-----
#record delete button click cheyagane pre_delete,post_delete signal panichesthai...

@receiver(pre_delete,sender=User) #This is @Decorator process
def at_beginning_delete(sender, instance, **kwargs): 
	print("-------------------------------")
	print("Pre Delete Signal.....")
	print("Sender:",sender)
	print('Instance:',instance)
	print(f'kwargs:{kwargs}')
#pre_delete.connect(at_beginning_delete,sender=User) #This is "Manual Connect Route" process	


		#----post_delete----

@receiver(post_delete,sender=User) #This is @Decorator process
def at_ending_delete(sender, instance, **kwargs): 
	print("-----------record Delete-------------")
	print("Post Delete Signal.....")
	print("Sender:",sender)
	print('Instance:',instance)
	print(f'kwargs:{kwargs}')
#post_delete.connect(at_ending_delete,sender=User) #This is "Manual Connect Route" process		

###############################################################

			#------pre_init--------

'''
Note: pre_init,post_init anedi runserver enter cheya gane http://127.0.0 rakamude
evi print auvthai..
'''			


@receiver(pre_init,sender=User) #This is @Decorator process
def at_beginning_init(sender, *args,**kwargs): 
	print("-------------------------------")
	print("Pre init Signal.....")
	print("Sender:",sender)
	print(f'Args:{args}')
	print(f'kwargs:{kwargs}')
#pre_init.connect(at_beginning_init,sender=User) #This is "Manual Connect Route" process	


	#----post_init----

@receiver(post_init,sender=User) #This is @Decorator process
def at_ending_init(sender, *args, **kwargs): 
	print("------------------------")
	print("Post init Signal.....")
	print("Sender:",sender)
	print(f'Args:{args}')
	print(f'kwargs:{kwargs}')
#post_init.connect(at_ending_init,sender=User) #This is "Manual Connect Route" process
##########################################################


	#------request_started------------
'''
Note: request_started, idi vachesi runserver click cheyana ne appudu http//	127.0.0
vasthundi kada.danini web browser lo enter cheyagane request_started signal active avuthundi
request_started complete aina tharuvatha request_finished active avuthundi. 
'''

@receiver(request_started) #This is @Decorator process
def at_beginning_request(sender, environ, **kwargs): 
	print("------------------------")
	print("At Beginning Request Signal.....")
	print("Sender:",sender)
	print('Environ:',environ)
	print(f'kwargs:{kwargs}')
#request_started.connect(at_beginning_request) #This is "Manual Connect Route" process


	#--------request_finished-----------

@receiver(request_finished) #This is @Decorator process
def at_ending_request(sender, **kwargs): 
	print("------------------------")
	print("At Ending Request Signal.....")
	print("Sender:",sender)
	print(f'kwargs:{kwargs}')
#request_finished.connect(at_ending_request) #This is "Manual Connect Route" process


	#--------got_request_exception----------
'''
Idi work cheyali ante views.py lo function rasi chusukovali....appudu web browser lo Error vasthundi ante
appudu 'at_req_exception' lowpala haa error ki code rasi execute cheyali.
'''

@receiver(got_request_exception) #This is @Decorator process
def at_req_exception(sender, request,**kwargs): 
	print("------------------------")
	print("At Request Exception.....")
	print("Sender:",sender)
	print('Request:',request)
	print(f'kwargs:{kwargs}')
#got_request_exception.connect(at_req_exception) #This is "Manual Connect Route" process


#####################################################################

'''
Note:pre_migrate,post_migrate pani cheyali ante munduga python manage.py migrate run 
cheyali.e command execute cheyagane "ee rendu migrate signals" kante mundu
konni signals pani chesthai... last ku matramu at_end_migrate_flush signal panichesthundi.

ee rendu signals only migrate chesinappudu matrame panichesthai...
'''

		#-------pre_migrate----------
	
@receiver(pre_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
	
	print("---------------------------------")
	print('before_install_app.........')
	print('Sender:',sender)
	print('App_config:',app_config)
	print('Verbosity:',verbosity)
	print('Interactive:',interactive)
	print('Using:',using)
	print('Plan:',plan)
	print('App:',apps)
	print(f'kwargs:{kwargs}')

#pre_migrate.connect(before_install_app)


		#-------post_migrate---------------

@receiver(post_migrate)
def at_end_migrate_flush(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
	
	print("---------------------------------")
	print('at_end_migrate_flush.........')
	print('Sender:',sender)
	print('App_config:',app_config)
	print('Verbosity:',verbosity)
	print('Interactive:',interactive)
	print('Using:',using)
	print('Plan:',plan)
	print('App:',apps)
	print(f'kwargs:{kwargs}')

#post_migrate.connect(at_end_migrate_flush)


################################################################3


	#---------connection_created-------

'''
connection_created,ee signal work cheyali ante muduga server run cheyali....run
chesi na tharuvatha carefull ga chudu okay na...	
'''

@receiver(connection_created)
def conn_db(sender,connection, **kwargs):
	print('------------------------')
	print('Initial Connection to the database........')
	print('Sender:',sender)
	print('Connection:',connection)
	print(f'kwargs:{kwargs}')
#connection_created.connect(conn_db)		



