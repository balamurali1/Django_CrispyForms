"""gs114_GenericEditing_lo_FormView_Topic URL Configuration

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
    path('contact/',views.ContactFormView.as_view(),name='contact'),
    path('thankyou/',views.ThanksTemplateView.as_view(),name='thankyou'),

    path('contact1/',views.FeedbackFormView.as_view(),name='contact1'),
    path('thankyou1/',views.FeedbackTemplateView.as_view(),name='thankyou1'),

]
