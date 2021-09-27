from django.contrib import admin
from enroll.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id','post_category','post_publish_date','user']
