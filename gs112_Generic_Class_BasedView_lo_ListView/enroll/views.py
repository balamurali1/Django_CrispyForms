from django.shortcuts import render
from enroll.models import Student
from django.views.generic.list import ListView

# Create your views here.

class StudentListView(ListView):
	model = Student  #ela single line lo rayavachunu..ee single line lo ne kindha comment lo unna 3lines,4 lines code untundi..

'''
Note : Model.py lo unde class Yooka objects(records) ni render(thisukovali ante)
cheyali ante simple ga "ListView" ni vadukoo..
'''


'''
Note: ela 3 lines,4 lines rayadam kanna code ni simple ga rayavachunu 
"ListView" ni use chesi single line lo rayavachunu.

	 stud = Student.objects.all()
	 context = {'student_list':stud}
	 return render(request,'enroll/student_list.html',context)

Note: ikkada context lo unde 'key' and html file names same undali okay na...
appudu data anedi browser lo kanipisthundi..
'''	