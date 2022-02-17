import re

from django.shortcuts import render
from django.views import generic
from .models import MainPageFragment, Meditation, Photo, Post, MainPagePhoto

def art_and_music(request):
  print(Photo.CATEGORY_CHOICES)
  pair_list = []
  print('ART AND MUSIC 1')
  for cat in Photo.CATEGORY_CHOICES:
    cat_photos = first = Photo.objects.filter(category=cat[0])
    if cat_photos:
      first = Photo.objects.filter(category=cat[0]).order_by('-created_on').first()
      second = first.get_category_display()
      third = second.lower().replace(' ', '-')
      pair = [first, second, third]
      pair_list.append(pair)  
    else:
      pair = None
      pair_list.append(pair)
  display = pair_list
  print(display)
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

def ministry(request):
  return render(request, 'ministry.html')

def music(request):
  return render(request, 'music.html')

def sacred_journeys(request):
  return render(request, 'sacred-journeys.html')

def spiritual_direction(request):
  return render(request, 'spiritual-direction.html')

#### Home #####
def home(request):
  #### governs text fragments on home page ####
  frag_a = MainPageFragment.objects.filter(role='tagline').get()
  frag_b = MainPageFragment.objects.filter(role='introduction').get()

  #### governs photos on home page ####
  SLIDESHOW = MainPagePhoto.ROLE_CHOICES[0][0]
  MENU = MainPagePhoto.ROLE_CHOICES[1][0]
  slideshow_images = MainPagePhoto.objects.filter(status=1, role=SLIDESHOW).order_by('order')
  menu_images = MainPagePhoto.objects.filter(status=1, role=MENU).order_by('order')
  pair_list = []
  for menu_image in menu_images:
    image = menu_image
    hyperlink_display = menu_image.get_hyperlink_display().lower().replace('_', '-')
    text_display = menu_image.get_hyperlink_display().upper().replace('_', ' ')
    print(text_display)
    pair = [image, hyperlink_display, text_display]
    pair_list.append(pair)
  for p in pair_list:
    print(p)
  return render(request, 'index.html', {
    'frag_a': frag_a,
    'frag_b': frag_b,
    'slideshow_images': slideshow_images,
    'menu_images': pair_list,
    # 'menu_images': menu_images,
    })

#### Blog #####
class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'blog/index.html'

def posts_index(request):
  posts = Post.objects.filter(status=1).order_by('-created_on')
  return render(request, 'blog/index.html', {'posts': posts})

class PostDetail(generic.DetailView):
  model = Post
  template_name = 'blog/post_detail.html'

#### Guided Meditations ####
def meditations_index(request):
  meditations = Meditation.objects.all()
  return render(
    request, 'guided-meditations.html', {'meditations': meditations}
    )