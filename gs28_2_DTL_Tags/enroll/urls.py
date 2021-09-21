from django.urls import path
from enroll.views import learn_django

urlpatterns = [
    path('learndj/',learn_django)
]
