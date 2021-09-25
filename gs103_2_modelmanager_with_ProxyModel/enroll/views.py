from django.shortcuts import render
from enroll.models import Student,ProxyStudent

# Create your views here.

def home(request):

	#student_data = Student.objects.all() #"objects" is model manager,this is by default,idi vachesi Student model table ki work auvthuni.
	#student_data = ProxyStudent.students.all()
	student_data = ProxyStudent.students.get_stu_roll_range(103,109) #"students" is model manager ,this is i am created in managers.py lo  manuvally
	
	return render(request,'enroll/home.html',{'student':student_data})

#Note: manamu cutommanager ni Proxystudent table lo echamu kabbati,customManager anedi ProxyStudent table ki work auvthundi.