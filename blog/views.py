from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.views.generic import ListView

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

class Search(ListView):
	template_name = 'blog/search.html'
	context_object_name='posts'

	def get_queryset(self):
		return Post.objects.filter(title__icontains=self.request.GET.get('search'))

	def get_contexr_data(self, *,object_list = None, **kwargs):
		return super().get.context_data(**kwargs)

		