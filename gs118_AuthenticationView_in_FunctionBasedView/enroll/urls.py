from django.urls import path
from enroll import views

urlpatterns = [
	path('profile/',views.profile,name='profile'),
]