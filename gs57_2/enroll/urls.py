from django.urls import path
from enroll import views

urlpatterns = [
	path('registration/',views.showinfo),
	path('success/',views.completed),
]