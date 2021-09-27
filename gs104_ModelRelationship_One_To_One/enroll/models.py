from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	#user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
	#user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff':True})
	page_name = models.CharField(max_length=70)
	page_cat = models.CharField(max_length=70)
	page_publish_date = models.DateField()


'''
Note: User ni delete chesthe daniki related records ani delete auvthai Page table lo okay na..

ippudu opposite direction lo chusthe Page table lo unde record ni delete chesthe
daniki related unna 'User record' anedi delete kadu.. idi anthey..
'''

'''
Note:ikkada by default ga User table anedi django ne esthundi.kabatti manamu create cheyaledu
ledu naku usertable auvasarma ledu anukunte nuv appudu new table ni create chesuko..

one-To-one lo oka user only one record matrame create cheyali pagetable lo malli malli create
cheyakudadu adi thisukodu kuda..

limit_choices_to={'is_staff':True}: Diniki artham vachesi is_staff unna valla list matrame page table lo unde
user field lo kanapadali ani artham.

Note:primary_key=True,ante Foreignkey ani artham.primary_key anedi User ane table lo unde
first column ni primary key antaru.Page ane class lo ki vasthundi
kabbati danini internal ga foreignkey ani pilusthamu. rasedemo primary_key=True ani rasthamu.

on_delete=models.CASCADE: Diniki artham vachesi User table lo unde record ni delete chesthe automatic ga
haa record ku related unna page table lo unde record kuda delete auvthundi.

on_delete=models.PROTECT: Diniki artham vachesi User table lo unde record ni delete chesthe
haa record ku related unna page table lo ni record ni "delete kakunda" chusthundi.

ledu compalsary record nu delete cheyali anukunte appudu "first" page table lo unde record ni
delete chesi haa record ku related unns User Table lo ni record ni delete cheyali..

(OR)

ledu "okay click" tho Page table lo unde record delete kavali haa record ku related unna  User table lo unde record
matrame delete kavali anukunte appudu 'signals' use chesi user table lo unde record ni
at the same delete cheyavachunu.

ela delete cheyali anukunappudu signal.py lo ki velli akkda chusi 'seder'lo echina table lo ki
velli akkadi nundi delete cheyali.'oka click' tho records delete auvthai..'
'''

