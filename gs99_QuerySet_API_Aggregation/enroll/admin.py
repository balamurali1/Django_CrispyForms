from django.contrib import admin
from enroll import models

# Register your models here.

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
	list_display=['id','name','roll','city','marks','passdate','admdatetime']