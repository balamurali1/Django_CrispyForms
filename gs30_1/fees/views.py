from django.shortcuts import render

# Create your views here.

def fees_python(request):
	return render(request,'fees/feesone.html',{'fees':300})