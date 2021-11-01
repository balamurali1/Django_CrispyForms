from django import forms
from eroll.models import User


class StudentRegistration(forms.ModelForm): #This class is parent class
	class Meta:
		model = User
		fields = ['student_name','email','password']

class TeacherRegistration(StudentRegistration): #This class is Chaild class,parent class all property assign to chalid class.
	class Meta(StudentRegistration.Meta):
		fields = ['teacher_name','email','password']
