from django.urls import path
from enroll import views


urlpatterns = [
    path('<int:my_id>/',views.show,name='detail'),
    path('<int:my_id>/<int:my_subid>/',views.showinfo,name='showdetail'),
    
]