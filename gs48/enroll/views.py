from django.shortcuts import render
from enroll import forms

# Create your views here
def showeinfo(request):
	fm = forms.StudentRegistration(auto_id=True,label_suffix=':-',
		initial={'name':'Your Name','email':'Your Email','last_name':'Last_Name'})

	con = {'form':fm}

	#fm.order_fields(field_order=None)
	#fm.order_fields(field_order=['last_name','email','name'])
	fm.order_fields(field_order=['name','last_name','email'])

	
	return render(request,'enroll/form.html',context = con)

