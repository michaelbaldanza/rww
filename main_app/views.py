import re

from django.shortcuts import render
from django.views import generic
from .models import MainPageFragment, Meditation, Photo, Post

def art_and_music(request):
  print(Photo.CATEGORY_CHOICES)
  pair_list = []
  for cat in Photo.CATEGORY_CHOICES:
    first = Photo.objects.filter(category=cat[0]).order_by('-created_on').first()
    second = first.get_category_display()
    third = second.lower().replace(' ', '-')
    pair = [first, second, third]
    pair_list.append(pair)  
  display = pair_list
  return render(
    request, 'art-and-music.html', {
      'display': display,
      }
    )

def photos_category(request, url_cat):
  for cat in Photo.CATEGORY_CHOICES:
    if cat[1].lower().replace(' ', '-') == url_cat:
      display = Photo.objects.filter(category=cat[0]).order_by('-created_on')
      print('PRINTING ITEM')
      print(display)
      for dis in display:
        print('PRINTING ITEM')
        print(dis)
      title = cat[1]
  return render(request, 'photo-cat.html', { 'display': display, 'title': title })

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

# Photos
def photos(request):
  photos = Photo.objects.all()
  mm_display = Photo.objects.filter(category='MM').order_by('-created_on').first()
  pe_display = Photo.objects.filter(category='PE').order_by('-created_on').first()
  pl_display = Photo.objects.filter(category='PL').order_by('-created_on').first()
  na_display = Photo.objects.filter(category='NA').order_by('-created_on').first()
  return render(
    request, 'photos.html', {
      'photos': photos,
      'mm_display': mm_display,
      'pe_display': pe_display,
      'pa_display': pl_display,
      'na_display': na_display
      }
    )

def photos_people(request):
  display = Photo.objects.filter(category='PE').order_by('-created_on')
  return render(request, {'display': display})

def photos_nature(request):
  display = Photo.objects.filter(category='NA').order_by('-created_on')
  pass

def photos_mystical(request):
  display = Photo.objects.filter(category='MM').order_by('-created_on')
  pass

def photos_places(request):
  display = Photo.objects.filter(category='PL').order_by('-created_on')
  pass