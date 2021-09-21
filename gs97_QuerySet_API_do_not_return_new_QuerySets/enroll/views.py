from django.shortcuts import render
from enroll.models import Student

# Create your views here.

def home(request):

############### get() ################

	student_data = Student.objects.get(pk=1)
		#(OR)
	#student_data = Student.objects.get(id=1)

#Note:Table lo unde first coloum ni 'primary(pk)' or 'id' ani antaru
#Note:pk ne id ani antaru,id ne pk ani antaru.
	
	#student_data = Student.objects.get(name='sonam')

############## first() ################

	#student_data = Student.objects.first()	
	#student_data = Student.objects.order_by('name').first()

############### last() #####################
	#student_data = Student.objects.last()
	#student_data = Student.objects.order_by('city').last()
	#student_data = Student.objects.order_by('name').last()

	
############# latest() ###############	

	#student_data = Student.objects.latest('pass_date')
	#student_data = Student.objects.latest('city')

############## earliest() ################
	#student_data = Student.objects.earliest('pass_date')
	#student_data = Student.objects.earliest('city')

############## exists() ################	
	'''
	student_data = Student.objects.all()
	print(student_data.exists())
	'''	


#Note:exists() method anedi data unda leda ani chusthundi,unte True vasthundi,ledu ante False vasthundi.

	'''
	student_data = Student.objects.all()
	one_date = Student.objects.get(pk=1)
	print(student_data.filter(pk=one_date.pk).exists())
	'''


################## CRUD Methods ######################

	####### create() ######

	#student_data = Student.objects.create(name='Sameer',roll=111,city='Secunderabad',marks = 72,pass_date='2021-09-20')

#Note:ela rasthe okay sari "create" auvhundi "save" auvthundi...


	########get_or_create() ###########
	'''
	Note:get_or_create()--> indu lo Two Methods unnai..get() and create()
	unna data nu malli esthe appudu get() work chesthundi.new data nu esthe appudu create() method
	pani chesthundi.
	'''

	#idi get() ga panichesindi
	#student_data,created =Student.objects.get_or_create(name='Sameer',roll=111,city='Secunderabad',marks = 72,pass_date='2021-09-20')
	
	#idi create() ga panichesindi
	#student_data,created =Student.objects.get_or_create(name='Bokar',roll=113,city='Secunderabad',marks = 23,pass_date='2021-09-22')


	############# update() ################
	#student_data = Student.objects.filter(id=12).update(name='Arjun Naik',city='Ongol')

	############### Multiple updates ###############
	#student_data = Student.objects.filter(city='Hyderand').update(marks = 0)


	############### update_or_create() ##############
	'''
	student_data,created = Student.objects.update_or_create(id = 10,name = 'Ashok',defaults = {'name':'kohli'})
	print(created)
	'''

	################# bulk_create() #################
	'''
	objs = [
	Student(name = 'Atif',roll = 114,city = 'Dhanbad',marks = 70,pass_date = '2020-5-4'),
	Student(name = 'Sahil',roll = 115,city = 'Bokaro',marks = 50,pass_date = '2020-5-6'),
	Student(name = 'kumar',roll = 116,city = 'Dhanbad',marks = 30,pass_date = '2020-5-9'),
	]
	student_data = Student.objects.bulk_create(objs) 
	'''

	############# bulk_update()#####################
	'''
	all_student_data = Student.objects.all()
	for stu in all_student_data:
		stu.city = "Dhanbad"  #--->  city column mootha ni ki 'Dhanbad' apply auvthundi.
	student_data = Student.objects.bulk_update(all_student_data,['city']) #['city']ante coloum name	
	'''


	################ in_bulk() ########################
	'''
	student_data = Student.objects.in_bulk([1,2]) #1,2 ante primarykey(pk),rows ani artham
	print(student_data[1].name) # 1(first) record lo ni name ni thisukunna ani artham
	print(student_data[2].marks)
	'''

	'''
	#Note: ikkada empty dictionary{} chupisthundi cmd lo 
	student_data = Student.objects.in_bulk([])
	'''

	'''
	#Note:ikkada total records chupisthundi.cmd lo
	student_data = Student.objects.in_bulk()
	'''

	################ delete() ###################

	'''
	#single record delete
	student_data = Student.objects.get(pk = 10).delete()
	'''

	'''
	#Multiple records delete
	student_data = Student.objects.filter(marks = 0).delete()
	'''

	'''
	#Anni delete cheyali ante all().delete()
	student_data = Student.objects.all().delete()
	'''

	############# count() #############
	'''
	#Table lo yenni records unnayaoo thelusukovachunu.ela
	student_data = Student.objects.all()
	print(student_data.count())
	'''

	print('Return:',student_data)
	return render(request,'enroll/home.html',{'student':student_data})