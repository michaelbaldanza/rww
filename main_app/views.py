from django.shortcuts import render
from django.views import generic
from .models import Post

def art(request):
  return render(request, 'art-and-music.html')

def home(request):
  return render(request, 'index.html')

def meditations(request):
  return render(request, 'guided-meditations.html')

def sacred(request):
  return render(request, 'sacred-journeys.html')

# Blog Views

class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
  model = Post
  template_name = 'blog/post_detail.html'