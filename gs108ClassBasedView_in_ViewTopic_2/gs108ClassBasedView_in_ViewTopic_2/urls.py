"""gs108ClassBasedView_in_ViewTopic_2 URL Configuration

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
    path('homefun/',views.homefun,name='homefun'),
    path('class/',views.HomeClassView.as_view(),name='class'),
    path('msg/',views.about,name='msg'),
    path('msgclass/',views.AboutClassView.as_view(),name='msgclass'),
    path('form/',views.contactfun,name='form'),
    path('classform/',views.ConntactFormView.as_view(),name='classform'),

    #path('new/',views.newsfun,name='new'),
    path('new/',views.newsfun,{'template_name':'enroll/new.html'},name='new'),
    path('newfun/',views.newsfun,{'template_name':'enroll/new1.html'},name='newfun'),

    #path('newclass/',views.NewClassView.as_view(),name='newclass'), #process-1
    path('newcls/',views.NewClassView.as_view(template_name='enroll/newclass.html'),name='newcls'), #process-2
    path('newc/',views.NewClassView.as_view(template_name='enroll/newcls.html'),name='newc'), #process-3


]
