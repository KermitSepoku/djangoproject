from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login , logout
from django.contrib.auth.models import User

def post_list(request):
    posts = Post.objects.filter()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def register(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('post_list')
	else:
		form = UserCreationForm() 
	return render(request, 'blog/login.html',{'form':form})

def user_login(request):
	if request.method =='POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('post_list')
	else:
		form = AuthenticationForm() 
	return render(request, 'blog/login.html',{'form':form})

def user_logout(request):
	logout(request)
	return redirect('login')

class Search(ListView):
	template_name = 'blog/search.html'
	context_object_name='posts'

	def get_queryset(self):
		return Post.objects.filter(title__icontains=self.request.GET.get('search'))

	def get_contexr_data(self, *,object_list = None, **kwargs):
		return super().get.context_data(**kwargs)


		