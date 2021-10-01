"""gs110ClassBsedView_lo_RedirectView URL Configuration

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

    #idi home page chudu okay na..
    path('',views.TemplateView.as_view(template_name='enroll/home.html'),name='blankhome'),

    path('PHP/',views.TemplateView.as_view(template_name='enroll/python.html'),name='php'),



    #url='/' ela pedithey root(home) window ki vellu ani artham
    path('python/',views.RedirectView.as_view(url='/'),name='python'),

    path('Script/',views.RedirectView.as_view(url='/something/'),name='script'),


	
	#pattern_name ni yenduku use chestharu ante, manamundu unde url lo yedo 
			#okadanini use chesukovadaniki..pattern_name use chestharu.
	
    #path('java/',views.RedirectView.as_view(url='/'),name='java')
    path('java/',views.RedirectView.as_view(pattern_name='php'),name='java'),
	#path('java/',views.RedirectView.as_view(pattern_name='script'),name='java'),
    
   
    path('tutorial/',views.RedirectView.as_view(url='https://www.tutorialsteacher.com'),name='tutorial'),

    path('tutorialpython/',views.RedirectView.as_view(url='https://www.tutorialsteacher.com/python'),name='tutorialpython'),

    path('tutorialsqlserver/',views.RedirectView.as_view(url='https://www.tutorialsteacher.com/sqlserver'),name='tutorialsqlserver'),

    path('tutorialtypescript/',views.GeekyshowsRedirectView.as_view(),name='tutorialtypescript'),

    #path('primary/<int:pk>/',views.GeekyRedirectView.as_view(),name='primary'), #idi url ki sambandam..(1)
    

    path('foreign/<str:pk>/',views.ShowsRedirectView.as_view(),name='foreign'),

    path('rootpage/<int:pk>/',views.AmazonRedirectView.as_view(),name='rootpage'),


    path('primary/<int:pk>/',views.GeekyRedirectView.as_view(),name='primary'),  # idi pattern_name ki sambandam.(1.1)
    path('<int:pk>/',views.TemplateView.as_view(template_name='enroll/page.html'),name='midpage'),

	
	#path('primary/<slug:post>/',views.GeekyRedirectView.as_view(),name='primary'),  # idi pattern_name ki sambandam.(1.1)
    #path('<slug:post>/',views.TemplateView.as_view(template_name='enroll/page.html'),name='midpage'),    


#Note: <int:pk> ikkada unna 'pk' vachesi url lo ki vachinappudu 'key' ga maruthundi..haa key ni html lo ki vachinappudu 'variable' ga maruthundi..  

]
