from django.urls import path
from enroll import views

urlpatterns = [
	path('learndj/',views.learn_django)
]
