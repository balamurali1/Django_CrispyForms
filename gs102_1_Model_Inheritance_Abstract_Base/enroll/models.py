from django.db import models
from django.utils import timezone

# Create your models here.

class BaseItem(models.Model):
	title = models.CharField(max_length=70)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True
		

class ItemA(BaseItem):
	content = models.TextField()	


class ItemB(BaseItem):
	file = models.FileField(upload_to='files')

class ItemC(BaseItem):
	file =models.FileField(upload_to='images')

class ItemD(BaseItem):
	slug  =models.SlugField(max_length=255,unique=True)


