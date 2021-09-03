from django.urls import path
from fees import views

urlpatterns = [
    path('dj/',views.learn_fees),
    path('python/',views.learn_python)
]
