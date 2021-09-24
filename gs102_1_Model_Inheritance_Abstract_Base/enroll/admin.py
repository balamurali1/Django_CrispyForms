from django.contrib import admin
from enroll.models import ItemA,ItemB,ItemC,ItemD

# Register your models here.

@admin.register(ItemA)
class ItemAAdmin(admin.ModelAdmin):
	list_display = ['id','title','created','updated','content']

@admin.register(ItemB)
class ItemBAdmin(admin.ModelAdmin):
	list_display = ['id','title','created','updated','file']

@admin.register(ItemC)
class ItemCAdmin(admin.ModelAdmin):
	list_display = ['id','title','created','updated','file']

@admin.register(ItemD)
class ItemDAdmin(admin.ModelAdmin):
	list_display = ['id','title','created','updated','slug']
