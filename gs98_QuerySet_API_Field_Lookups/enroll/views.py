from django.shortcuts import render
from enroll.models import Student
from datetime import date
from datetime import time


# Create your views here.

def home(request):

######### all() ######
	student_data = Student.objects.all()


##########filter()##########
#Note:__exact idi casecensitive(unnadi unnatlu ga type cheyali) matrame esthundi.
	#student_data = Student.objects.filter(name__exact='sonam')#incasecensitive	
	#student_data = Student.objects.filter(name__exact='Sonam') #casecensitive


#Note:__iexact anedi casecensitive gurinchi pattinchukodu echina name ni batti related names ni chupisthundi.
	#student_data = Student.objects.filter(name__iexact='Sonam')


#Note:__contains ante name lo oka letter thusukoni haa letter ki related unna names ani ravali
	#student_data = Student.objects.filter(name__contains='u')


#Note:__icontains anedi casecensitive gurinchi pattinchukodu,ante name lo oka letter thusukoni haa letter ki related unna names ani ravali	
	#student_data = Student.objects.filter(name__icontains='U')


#Note:__in ante table lo unde data lo particular data kavali ante ela

	#student_data = Student.objects.filter(id__in=[1,5,7])

	#student_data = Student.objects.filter(marks__in=[60])
	#student_data = Student.objects.filter(marks__in=[60,70,50])

	#student_data = Student.objects.filter(marks__gt=60)
	#student_data = Student.objects.filter(marks__gte=60) #gte ante 60 kuda vasthundi


	#student_data = Student.objects.filter(marks__lt=70)
	#student_data = Student.objects.filter(marks__lte=70) #lte ante 70 kuda vasthundi


#Note:__startswith,__endswith anevi casecensitive ni pattinchukodu

	#student_data = Student.objects.filter(name__startswith='s')
	#student_data = Student.objects.filter(name__startswith='S')

	#student_data = Student.objects.filter(name__istartswith = 's')
	#student_data = Student.objects.filter(name__istartswith = 'S')

	#student_data = Student.objects.filter(name__endswith = 'l')
	#student_data = Student.objects.filter(name__endswith = 'L')

	#student_data = Student.objects.filter(name__iendswith = 'L')
	#student_data = Student.objects.filter(name__iendswith = 'l')


#Note:__range 
	#student_data = Student.objects.filter(passdate__range=('2020-04-04','2020-05-10'))
	#student_data = Student.objects.filter(passdate__range=('2020-04-01','2020-05-10'))
	#student_data = Student.objects.filter(passdate__range=('2020-04-01','2020-05-03'))

#Note:Particular date ki sambandinchina data kavali ante import cheyali datetime ni first paina....
	
	#student_data = Student.objects.filter(admdatetime__date = date(2020,1,3))
	#student_data = Student.objects.filter(admdatetime__date = date(2020,1,2))

	#student_data = Student.objects.filter(admdatetime__date__gt = date(2020,1,2))
	
	#student_data = Student.objects.filter(admdatetime__date__lt = date(2020,1,4))


#Note: __year particular year records kavali ante ela..	

	#student_data = Student.objects.filter(passdate__year = 2019)
	
	#student_data = Student.objects.filter(passdate__year__gt = 2019)

	#student_data = Student.objects.filter(passdate__year__gte= 2019)

#Note: __month

	#student_data = Student.objects.filter(passdate__month = 4)
	#student_data = Student.objects.filter(passdate__month__gt = 4)
	#student_data = Student.objects.filter(passdate__month__gte = 4)
	
	#student_data = Student.objects.filter(passdate__month = 5)

#Note:__day
	#student_data = Student.objects.filter(passdate__day = 2)
	#student_data = Student.objects.filter(passdate__day__gt = 2)
	#student_data = Student.objects.filter(passdate__day__lt = 7)
	#student_data = Student.objects.filter(passdate__day__lte = 7)

#Note; __week,year lo vachesi 52 weeks untai, 14 week lo ye month and ye date vachindo chudavachunu.
	#student_data = Student.objects.filter(passdate__week =14)

	#student_data = Student.objects.filter(passdate__week__gt =14)

	#student_data = Student.objects.filter(passdate__week =10)
	#student_data = Student.objects.filter(passdate__week = 19)



#__week_day_5,  EX:1 ante sunday nundi start auvthundi,1 ante sunday kada. appudu sunday related records esthundi.
	# 1-7 ante (sunday to studerday) ani..

	#student_data = Student.objects.filter(passdate__week_day = 5)
	#student_data = Student.objects.filter(passdate__week_day = 3)
	#student_data = Student.objects.filter(passdate__week_day = 6)
	#student_data = Student.objects.filter(passdate__week_day = 2)

	#student_data = Student.objects.filter(passdate__week_day__gt = 5)



#Note:Jan to Mar(1 quarter),Apr to Jun(2 quarter),july to sep(3 quarter),Oct to Dem(4 quarter)
# __quarter

	#student_data = Student.objects.filter(passdate__quarter = 2)
	#student_data = Student.objects.filter(passdate__quarter__lt = 5)


# __time
	#student_data = Student.objects.filter(admdatetime__time__gt = time(6,00))
	#student_data = Student.objects.filter(admdatetime__time__gt = time(21,17))

#Note:__hour, hour's(0 to 23)
	#student_data = Student.objects.filter(admdatetime__hour = 6)
	#student_data = Student.objects.filter(admdatetime__hour__gt = 6)

#NOte: __minute, minute(0 to 59)
	#student_data = Student.objects.filter(admdatetime__minute =25 )
	#student_data = Student.objects.filter(admdatetime__minute__gt =26 )
	#student_data = Student.objects.filter(admdatetime__minute__gt =20 )

# __second  
	#student_data = Student.objects.filter(admdatetime__second__gt =20 )
	#student_data = Student.objects.filter(admdatetime__second =20 )

# __isnull
	#student_data = Student.objects.filter(roll__isnull = True ) #isnull=True ani pedithey data radu
	#student_data = Student.objects.filter(roll__isnull = False ) #isnull = False ani pedithey data vasthundi


	

	print('Return:',student_data)
	print()
	print("SQL Query:",student_data)

	return render(request,'enroll/home.html',{'student':student_data})
