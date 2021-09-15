from django.shortcuts import render


# Create your views here.

# def showinfo(request,my_id):
# 	return render(request,'enroll/user.html')


def showinfo(request,my_id):
	return render(request,'enroll/user.html',{'id':my_id})

		