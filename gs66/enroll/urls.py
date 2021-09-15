from django.urls import path
from enroll import views

urlpatterns = [
	path('student/<my_id>/',views.showinfo,name='detail'),

]

#<my_id>-->ela rasthe idi (integer ni,string ni)accept chesthundi URL lo ..."all-in-one" ani artham vasthundi..