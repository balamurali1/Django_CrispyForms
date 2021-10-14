"""gs121_classBasedView_in_loginrequired_staffmemberrequired URL Configuration

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
from django.urls import path,include
from registration import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')), #idi direct ga url lo login open cheyavachunu
    path('accounts/',include('registration.urls')),  #idi profile page ni chupisthundi
    
    path('about/',login_required(views.AboutTemplateView.as_view()),name='about'),

    path('staff/',staff_member_required(views.StaffTemplateView.as_view()),name='staff'),
    #Note: admin.site ni logout chesukuntu try chesthu undali..

    

]
