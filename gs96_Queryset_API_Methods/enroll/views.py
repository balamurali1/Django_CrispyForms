from django.shortcuts import render
from enroll.models import Student,Teacher
from django.db.models import Q

# Create your views here.

def home(request):

			#---------all()---------#
	student_data = Student.objects.all()


			#---------filter()--------#
	#student_data = Student.objects.filter(marks=60)


			#--------exclude()--------#
	#student_data = Student.objects.exclude(marks=60) #Dinini vadilesi migathavi chupinchu ani..


		#-------order_by()------------#
	#student_data = Student.objects.order_by('city')
	#student_data = Student.objects.order_by('roll')
	#student_data = Student.objects.order_by('name') #ASC order--->Ascending order	
	#student_data = Student.objects.order_by('-name') #Desc order --->Desending order
	#student_data = Student.objects.order_by('?') #'?'-->idi pettina tharuvatha page ni refresh chesthe "jambling" auvthu untai..
	#student_data = Student.objects.order_by('id')
	#student_data = Student.objects.order_by('id').reverse()
	#student_data = Student.objects.order_by('id')[:5]
	#student_data = Student.objects.order_by('id')[2:6]
	#student_data = Student.objects.order_by('id')[1:9:2]
	#student_data = Student.objects.order_by('id').reverse()[3:]
	#student_data = Student.objects.order_by('id').reverse()[1:6]
	#student_data = Student.objects.order_by('id').reverse()[0:4]
	#student_data = Student.objects.order_by('id').reverse()[1:10:3]

		#-----------values()----------#
	#student_data = Student.objects.values()
	#student_data = Student.objects.values('id','name','pass_date')
	#student_data =  Student.objects.values('id','roll','city')
	#student_data = Student.objects.values('id','name')


		#------values_list(idi ni ki named=True pettali browser lo kanipisthundi--------#

	#student_data = Student.objects.values_list()	
	#student_data = Student.objects.values_list('id','name')
	#student_data = Student.objects.values_list('id','city',named = True)
	#student_data = Student.objects.values_list('id','marks','pass_date',named = True)


	#---------using('default')---ela pedithey mootham data kanipisthundi----#

	#student_data = Student.objects.using('default')


	#-----dates(field,kind(year or month or week or day ),order='ASC')----#

	#student_data = Student.objects.dates('pass_date','month',order='ASC')
	#student_data = Student.objects.dates('pass_date','year',order='DESC')
	#student_data = Student.objects.dates('pass_date','day') #by default ASC order
	#student_data = Student.objects.dates('pass_date','week',order='DESC')


	#---none() emi chupinchadu browser lo kabbati error vachinattlu chupisthundi----------#
	#student_data = Student.objects.none()

########## Teacher ##################


	############ union() #############
	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True	)
	# student_data = qs2.union(qs1)  # qs2 table lo ki qs1 table ni combine cheshanu ani artham
				#(OR)
	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True	)
	# #student_data = qs2.union(qs1,all=False) # by default all=False
	# student_data = qs2.union(qs1,all=True)



	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True	)
	# student_data = qs1.union(qs2)  # qs1 table lo ki qs2 table ni combine cheshanu ani artham
				#(OR)
	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True	)
	# #student_data = qs1.union(qs2,all=False) ## by default all=False
	# student_data = qs1.union(qs2,all=True)

#Note: okay table lo ne multiple tables ni combine cheyali ante ela example ga chupistha chudu
			#student_data = qs1.union(qs2,qs3,qs4,qs5, all=True)


############### Intersection() #####################	

#EX:id same undi ,name same unte ikkada chupisthundi.

	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True	)
	# student_data = qs2.intersection(qs1) #intersection ante first table lo second table lo same to same data undali.echina fields ni batti
	
	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True	)
	# student_data = qs1.intersection(qs2)
	

########## difference ##############3
	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True	)
	# student_data = qs1.difference(qs2) #qs1 - qs2


	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True	)
	# student_data = qs2.difference(qs1) #qs2 - qs1


################# AND(&) ##########

	#student_data = Student.objects.filter(id = 6) & Student.objects.filter(roll = 106)
	#student_data = Student.objects.filter(roll = 105) & Student.objects.filter(city = 'Bukaro')
		#(OR)
	#student_data = Student.objects.filter(roll = 106,city='Hyderand')
#Note: AND ni shortcut lo rayali ante ela comma(,)peeti rayavachunu..


#Note: AND ni shortcut lo rayali ante inko vidhan ga  "Q" object ni use cheyavachunu.(import chesukovali)	
	#student_data = Student.objects.filter(Q(id=8) & Q(roll=108))


################# or (|) ##########	
#Note: or operator lo yela ante both side true aithey both records print auvthai

	#student_data = Student.objects.filter(id = 6) | Student.objects.filter(roll = 106) 
	#student_data = Student.objects.filter(id = 6) | Student.objects.filter(roll = 120)
	#student_data = Student.objects.filter(Q(id=6) | Q(roll=108))
	#student_data = Student.objects.filter(Q(id=0) | Q(roll=108))



	print("Return:",student_data) #ela rasthe cmd lo chudavachunu
	print()
	print("SQL Query:",student_data.query)
	return render(request,'enroll/home.html',{'students':student_data})
