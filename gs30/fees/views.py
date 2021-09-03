from django.shortcuts import render

# Create your views here.

def learn_fees(request):
	return render(request,'fees/feesone.html',{'fees':300})
