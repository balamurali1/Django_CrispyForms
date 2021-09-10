from django.urls import path
from enroll import views

urlpatterns = [
	path('stu/',views.home1),
	path("student/",views.create_stu),
	path("student_update/<int:pk>/",views.create_update),


	path('stu1/',views.home2),
	path("student1/",views.create_mark),
	path("student_update1/<int:pk>/",views.mark_update),

]	