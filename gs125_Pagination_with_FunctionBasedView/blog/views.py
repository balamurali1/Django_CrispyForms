from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator

# Create your views here.

def post_list(request):
	all_post = Post.objects.all().order_by('id')  #objects means rows ani artham okay na..

	'''
	syntax:
		p = Paginator(list_of_objects, no_of_objects_per_page)
	'''
	#paginator = Paginator(all_post,3)
	paginator = Paginator(all_post,3,orphans=1)

	page_number = request.GET.get('page')
	
	page_obj = paginator.get_page(page_number)

	return render(request,'blog/home.html',context={'page_obj':page_obj})
