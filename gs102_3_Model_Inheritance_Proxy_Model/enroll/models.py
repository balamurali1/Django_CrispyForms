from django.db import models

# Create your models here.

#Note:proxy ante ne Base class,chaild class Behaviours(data ni artham) same untai.base class yooka 
	#filed's chaild class ki apply auvthai.


class ExamCenter(models.Model): #parent class
	cname= models.CharField(max_length=70)
	city = models.CharField(max_length=70)

class StudentCenter(ExamCenter): #chaild class
	class Meta:
		proxy = True  #ela pettinappudu parent lo unde fields ani chaild lo ki vasthai.
		
		#ordering = ['city'] #passitive pedithey [A to z]
		ordering = ['-city'] #negative pedithey [z to A]


		#ordering = ['id'] # this is by default, passitive pedithey 1,2,3,4,...	
		#ordering = ['-id'] #negative pedithey 4,3,2,1...


'''
Note: ordering ante paticular column lo unde name's alphabetical order lo ravali ante
ordering use chestharu.idi admin site lo  changing kanipisthundi.

anthey kakunda proxy model chesetappudu SQLite database lo only parent table matrame
create auvthundi..
''' 

'''
Note:proxy model use echinappudu tables lo gani data base lo gani same to same to "data" vasthai
parent table lo enter chesthe data automatice ga chaild table lo kuda data same vasthundi
chaild table lo enter chesthe data automatice ga parent table lo kuda data same vasthundi
" it is opposite process". each and every column lo same to same data vasthundi


Note: chaild table lo matrame data anedi different order lo ravali ante order chane cheyali.
'''			