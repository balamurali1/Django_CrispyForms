from django.contrib import admin
from enroll.models import Customer,Product,Tag,Order

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
	
