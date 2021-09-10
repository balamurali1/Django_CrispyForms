from django import forms
from enroll.models import Student_list_table,Student_mark_table

class Student_list(forms.ModelForm):
	class Meta:
		model = Student_list_table
		fields = ['name','roll_number','date_of_birth']

class Student_mark(forms.ModelForm):
	class Meta:
		model=Student_mark_table
		fields=['student','marks']		


