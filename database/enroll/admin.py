from django.contrib import admin
from enroll.models import Student,Address

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['id','name','age']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	list_display = ['id','city','phone']
