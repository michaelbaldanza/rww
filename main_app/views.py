from django.shortcuts import render
from django.views import generic
from .models import Post

def art(request):
  return render(request, 'art-and-music.html')

def home(request):
  return render(request, 'index.html')

def meditations(request):
  return render(request, 'guided-meditations.html')

def ministry(request):
  return render(request, 'ministry.html')

def music(request):
  return render(request, 'music.html')

def photography(request):
  return render(request, 'photography.html')

def sacred_journeys(request):
  return render(request, 'sacred-journeys.html')

def spiritual_direction(request):
  return render(request, 'spiritual-direction.html')

# Blog Views

class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
  model = Post
  template_name = 'blog/post_detail.html'