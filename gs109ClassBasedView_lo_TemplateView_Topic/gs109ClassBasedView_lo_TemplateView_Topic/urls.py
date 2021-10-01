"""gs109ClassBasedView_lo_TemplateView_Topic URL Configuration

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

    path('',views.TemplateView.as_view(template_name = 'enroll/home.html'),name='home'),

    path('index/',views.TemplateView.as_view(template_name = 'enroll/index.html'),name='index'),

    path('viewcls/',views.HomeTemplateView.as_view(),name='home'),

   	path('page/',views.PageTemplateView.as_view(),name='page'),
    
    path('extra/',views.ExTemplateView.as_view(extra_context={'course':'Python'}),name='page'),

    path('kwargs/<int:cls>/',views.KeyArgView.as_view(),name='kwargs'),#<int:cls> cls is key

    
]
