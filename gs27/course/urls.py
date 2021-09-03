from django.urls import path
from course import views

urlpatterns = [
	path('learndj/',views.learn_django),
	path('learnpy/',views.learn_python),
	path('learnjv/',views.learn_java),
	path('learnphp/',views.learn_php),
]