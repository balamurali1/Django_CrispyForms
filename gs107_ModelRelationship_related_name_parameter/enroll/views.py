from django.shortcuts import render
from enroll.models import Page,Post,Song,User

# Create your views here.

def home(request):
	return render(request,'enroll/home.html')

def show_user_data(request):
	data1 = User.objects.all()
	data2 = User.objects.filter(email='rahul@gmail.com')
	data3 = User.objects.filter(mypage__page_cat ='Programming')
	data4 = User.objects.filter(mypost__post_publish_date='2021-09-17')
	data5 = User.objects.filter(mysong__song_duration=3)
	
	return render(request,'enroll/user.html',{'data1':data1,'data2':data2,
		'data3':data3,'data4':data4,'data5':data5})

'''
Note:
EX:data3 = User.objects.filter(mypage__page_cat = 'PHP')	diniki artham emity ante

User ane athanu mypage(Page)model lo ni class lo unde field(column) ni filter chesthunadu ani artham.
'''


def show_page_data(request):
	data1 = Page.objects.all()
	data2 = Page.objects.filter(page_cat = 'News')
	data3 = Page.objects.filter(user__email = '	muralid@gamil.com')
	return render(request,'enroll/page.html',{'data1':data1,'data2':data2,'data3':data3})



def show_post_data(request):
	data1 = Post.objects.all()
	data2 = Post.objects.filter(post_publish_date = '2021-09-03')
	data3 = Post.objects.filter(user__username = 'admin')
	return render(request,'enroll/post.html',{'data1':data1,'data2':data2,'data3':data3})



def show_song_data(request):
	data1 = Song.objects.all()
	data2 = Song.objects.filter(song_duration = 5)
	data3 = Song.objects.filter(user__username = 'Murali')
	return render(request,'enroll/song.html',{'data1':data1,'data2':data2,'data3':data3})