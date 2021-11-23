import re

from django.shortcuts import render
from django.views import generic
from .models import MainPageFragment, Meditation, Post

def art_and_music(request):
  return render(request, 'art-and-music.html')

# def home(request):
#   return render(request, 'index.html')

# def home(request):
#   # tl = HomeText.objects.filter(role='tagline')
#   # print(tl)
#   # print(tl.role)
#   home_texts = HomeText.objects.all()
#   return render(request, 'index.html', {'home_texts': home_texts})

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

#Home
def home(request):
  frag_a = MainPageFragment.objects.filter(role='tagline').get()
  frag_b = MainPageFragment.objects.filter(role='introduction').get()
  return render(request, 'index.html', {'frag_a': frag_a, 'frag_b': frag_b})

# Blog
class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
  model = Post
  template_name = 'blog/post_detail.html'

# Guided Meditations
class MeditationList(generic.ListView):
  queryset = Meditation.objects.filter(status=1).order_by('-created_on')
  template_name = 'guided-meditations.html'

def meditations_index(request):
  meditations = Meditation.objects.all()
  return render(
    request, 'guided-meditations.html', {'meditations': meditations}
    )