from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	page_name = models.CharField(max_length=70)
	page_cat = models.CharField(max_length=70)
	page_publish_date = models.DateField()

class Like(Page):
	page = models.OneToOneField(Page,on_delete=models.CASCADE,primary_key=True,parent_link=True)
	likes = models.IntegerField()


'''
Note: Like table anedi 'page' ane table ni 'inheritance' chesukundi appudu Like table
lo ki page table lo unde fields ani vasthai automatic ga..

anthey kakunda data enter chesetappudu Like table lo enter chesthe automatice ga
Page table lo ki vachesthai.kani Page table lo data enter chesthe Like table lo ki
data anedi radu...gurthupettuko..
'''

'''
Note: User ni delete chesthe daniki related records ani delete auvthai Page,Like table lo okay na..

ippudu opposite direction lo chusthe Page,Like table lo unde record ni delete chesthe
daniki related unna 'User record' anedi delete kadu.. idi anthey..
'''