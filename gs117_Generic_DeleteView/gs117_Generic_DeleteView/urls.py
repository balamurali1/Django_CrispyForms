"""gs117_Generic_DeleteView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',views.StudentCreateView.as_view(),name = 'stucreate'),
    path('thanks/',views.ThanksTemplateView.as_view(),name = 'thankyou'),
    path('update/<int:pk>/',views.StudentUpdateView.as_view(),name = 'stuupdate'),
    path('thanksupdate/',views.ThanksUpdateTemplateView.as_view(),name = 'thankyouupdate'),
    path('delete/<int:pk>/',views.StudentDeleteView.as_view(),name = 'studelete'),
]
