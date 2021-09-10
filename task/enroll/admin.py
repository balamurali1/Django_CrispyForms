from django.contrib import admin
from enroll.models import Student_list_table,Student_mark_table

# Register your models here.
for model in [Student_list_table,Student_mark_table]:
	admin.site.register(model)
