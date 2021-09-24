from django.contrib import admin
from enroll.models import ExamCenter,StudentCenter

# Register your models here.

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
	list_display = ['id','cname','city']

@admin.register(StudentCenter)
class StudentCenterAdmin(admin.ModelAdmin):
	list_display = ['id','cname','city']

