# Python Imports
import re, warnings
from urllib import request as ulreq
from PIL import ImageFile
from datetime import date

# Helper functions

def getsizes(uri):
    warnings.filterwarnings("ignore", "(Possibly )?corrupt EXIF data", UserWarning)
    # get file size *and* image size (None if not known)
    file = ulreq.urlopen(uri)
    size = file.headers.get("content-length")
    if size: 
        size = int(size)
    p = ImageFile.Parser()
    while True:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return size, p.image.size
            break
    file.close()
    return(size, None)

# Django Imports
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .models import MainPageFragment, Meditation, Photo, Post, MainPagePhoto, SacredJourney, MinisterialRecord, MinisterialRecordImage

def art_and_music(request):
  pair_list = []
  for cat in Photo.CATEGORY_CHOICES:
    photo_dict = {}
    cat_photos = first = Photo.objects.filter(category=cat[0])
    if cat_photos:
      first = Photo.objects.filter(category=cat[0]).order_by('-created_on').first()
      photo = Photo.objects.filter(category=cat[0]).order_by('-created_on').first()
      photo_dict['url'] = photo.photo_link
      second = photo.get_category_display()
      photo_dict['group_name'] = photo.get_category_display()
      third = second.lower().replace(' ', '-')
      photo_dict['group_path'] = photo.get_category_display().lower().replace(' ', '-')
      print(photo_dict)
      if photo:
        print('**********PRINTING PHOTO_DICT **********')
        size = getsizes(photo_dict['url'])
        photo_dict['width'] = size[1][0]
        photo_dict['height'] = size[1][1]
        photo_dict['aspect_ratio'] = photo_dict['width'] / photo_dict['height']
        print(photo_dict['group_name'])
        print(photo_dict['width'])
        print(photo_dict['height'])
        print(photo_dict['aspect_ratio'])
      pair = [first, second, third]
      pair_list.append(pair)  
    else:
      pair = None
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

def ministry(request):
  return render(request, 'ministry.html')

@login_required
def ministerial_record(request):
  min_rec = MinisterialRecord.objects.get()
  min_images = MinisterialRecordImage.objects.order_by('position')
  print(min_images)
  # print(min_rec.pastoral_care)
  # this is not working
  context = {
    'min_rec': min_rec,
    'min_images': min_images
  }
  print(context)
  context['min_rec'].pastoral_care
  return render(request, 'ministerial-record.html', context)

def music(request):
  return render(request, 'music.html')

### Sacred Journeys ###
def sacred_journeys_index(request):
  journeys = SacredJourney.objects.filter(status=1).order_by('-created_on')
  today = date.today()
  upcoming_journeys = []
  previous_journeys = []
  for journey in journeys:
    print(journey.banner_picture)
    print(today)
    if journey.start_date > today:
      upcoming_journeys.append(journey)
    else:
      previous_journeys.append(journey)
  print(upcoming_journeys)
  print(previous_journeys)
  return render(
    request,
    'sacred-journeys/index.html',
    {
      'upcoming_journeys': upcoming_journeys,
      'previous_journeys': previous_journeys
    },
    )

class SacredJourneyDetail(generic.DetailView):
  model = SacredJourney
  template_name = 'sacred-journeys/detail.html'

class SacredJourneyUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'sacred_journey.update_sacred_journeys'
  model = SacredJourney
  fields = '__all__'

class SacredJourneyDelete(PermissionRequiredMixin, DeleteView):
  permission_required = 'sacred_journey.delete_sacred_journey'
  model = SacredJourney
  success_url = '/sacred-journeys/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

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
    print('DEFAULT HYPERLINK DISPLAY')
    print(menu_image.get_hyperlink_display())
    hyperlink_display = menu_image.get_hyperlink_display().lower().replace('_', '-')
    text_display = menu_image.get_hyperlink_display().replace('_', ' ').title()
    print(text_display)
    pair = [image, hyperlink_display, text_display]
    pair_list.append(pair)
  for p in pair_list:
    print(p)

  num_visits = request.session.get('num_visits', 0)
  request.session['num_visits'] = num_visits + 1
  print(request.user)
  print('# of visits:')
  print(num_visits)

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
  # print('printing request info')
  # print(request.user.get_all_permissions())
  posts = Post.objects.filter(status=1).order_by('-created_on')
  for post in posts:
    if post.image:
      print(post.image)
  return render(request, 'blog/index.html', {'posts': posts})

class PostDetail(generic.DetailView):
  model = Post
  template_name = 'blog/post_detail.html'

class PostCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'post.add_posts'

  model = Post
  fields = ['title', 'author', 'content', 'status', 'image_source', 'image']

  # def test_func(self):
  #   print(self.request.user)
  #   return self.request.user.email.endswith('@example.com')

class PostUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'post.update_posts'
  model = Post
  fields = ['title', 'content', 'status', 'image_source', 'image']

class PostDelete(PermissionRequiredMixin, DeleteView):
  permission_required = 'post.delete_posts'
  model = Post
  success_url = '/blog/'

#### Guided Meditations ####
def meditations_index(request):
  meditations = Meditation.objects.all()
  return render(
    request, 'guided-meditations.html', {'meditations': meditations}
    )