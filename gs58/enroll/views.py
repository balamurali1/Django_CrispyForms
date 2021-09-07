from django.shortcuts import render
from enroll.forms import ContactForm,SubcriptionForm
from django.http import HttpResponseRedirect

# Create your views here.
def close(request):
	return render(request,'enroll/close.html')


def multiple_forms(request):
	if request.method=='POST':
		contact_form=ContactForm(request.POST)
		subcription_form =SubcriptionForm(request.POST)
		if contact_form.is_valid() or subcription_form.is_valid():
			print('ContactForm is Validations!!')
			print('SubcriptionForm is Validations!!')

			return HttpResponseRedirect('/regi/close/')

	else:
		contact_form=ContactForm()
		subcription_form=SubcriptionForm()

	return render(request,'enroll/user.html',{'con':contact_form,'sub':subcription_form})				