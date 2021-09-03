from django.urls import path
from fees import views

urlpatterns = [
	path('learnfees/',views.fees_python)
	
]