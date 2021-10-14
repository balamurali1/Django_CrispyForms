from django.shortcuts import render,HttpResponseRedirect
from enroll.models import User
from enroll.forms import StudentRegistration
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

# Create your views here.

#This Class will ADD new  items and show All Items
class UserAddShowView(TemplateView): #TemplateView ante create cheyadaniki use chestharu
		#--------- get() process --------------
	template_name = 'enroll/addandshow.html'
	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs) #ikkada super() vachesi,UserAddShowView ani artham.
		fm = StudentRegistration()  #ikada blank form chupisthundi.
		stud = User.objects.all()
		context = {'stu':stud,'form':fm}
		return context

			#--------- post() process (create) ---------
	def post(self,request):
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			nm = fm.cleaned_data['name']  #cleaned_data= ante get()ani artham
			em = fm.cleaned_data['email']
			pw = fm.cleaned_data['password']
			reg = User(name = nm,email = em,password = pw)
			reg.save()
			fm = StudentRegistration()
		return HttpResponseRedirect('/') # '/'ela rasthe home lo ravali ani artham
'''
Note: function based view lo by default ga get()method untundi,kani class based
view lo get() method undadu kabbati appudu saparet ga get() call chersukovali.
oka method ni rasthunamu ante mandatory ga 'self' parameter undali,'request' parameter
vachesi manaku auvsaramu unachota think chesukoni  call chesukovali.like update(get),create(post)...etc 

note:class based view lo get() ledu kabbati get method rasukovali alage post() ledu
kabbati post method rasukovali. ee la ga yee method lekunte haa method rasukovali.
'''

			
#This Class Based will Update/Edit
class UserUpdateView(View):  #View ante update cheyadaniki vadutharu
	def get(self, request, id):
		pi = User.objects.get(pk = id)
		fm = StudentRegistration(instance = pi)
		return render(request,'enroll/updatestudent.html',{'form':fm})

	def post(self,request,id):
		pi = User.objects.get(pk = id) #pk=id ante pk,id equal undali ani artham.
		fm = StudentRegistration(request.POST,instance = pi) #instance(object)=pi ante,particular data nu 'fm' ki assign cheyadam
		if fm.is_valid():
			fm.save()

		#return render(request,'enroll/updatestudent.html',{'form':fm})
		#(or)		
		return HttpResponseRedirect('/')


#This Class Based Will DELETE
class UserDeleteView(RedirectView):  #RedirectView ante delete cheyadaniki use chestharu
	url  ='/'
	def get_redirect_url(self,*args,**kwargs):
		del_id = kwargs['id'] #Ex:kwargs ante ela dictionary lo vasthundi{'id':6},get cheyali ante ela.. kwargs['id']
		User.objects.get(pk = del_id).delete()

		return super().get_redirect_url(*args,**kwargs)



