from django.shortcuts import render
from enroll.models import Student

# Create your views here.

def home(request):

	student_data = Student.students.get_stu_roll_range(101,104)

	context = {'student':student_data}

	return render(request,'enroll/home.html',context = context)
'''
note:ikada	get_stu_roll_range() method ni managers.py unde dani ikkada call cheshanu.
idi actually ga filer() use cheshamu. filter ni view.py lo ne call cheyali ani emi ledu
filter ki suppart ga method rasi managers.py ela call cheyavachunu.managers.py lo ne filter condition ehi
ela rayavachunu. ala manager.py lo chala filter conditions ela ne rasukovachunu.
'''