from django.urls import path
from enroll import views

urlpatterns = [
	path('info/<int:id>/',views.studentinfo)
	
]