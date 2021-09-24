from django.shortcuts import render
from enroll.models import ItemA,ItemB,ItemC,ItemD

# Create your views here.

def home(request):
	a = ItemA.objects.all()
	b = ItemB.objects.all()
	c = ItemC.objects.all()
	d = ItemD.objects.all()

	context = {'a':a,'b':b,'c':c,'d':d}

	return render(request,'enroll/home.html',context = context)

