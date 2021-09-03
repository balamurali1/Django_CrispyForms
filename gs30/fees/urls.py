from django.urls import path
from fees import views

urlpatterns = [
	path('learnfee/',views.learn_fees),
]