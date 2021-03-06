# Python Imports
import re, warnings
from datetime import date

S3_PREFIX = 'https://revwaynew.s3.amazonaws.com/'

# Helper function
def make_menu_strings(record):
  if record:
    image_title_pairs = []
    for pair in record.get_fields():
      if 'image' in pair[0]:
        image_dict = {
          'text': pair[0].replace('_', ' ').replace(' image', ''),
        }
        if pair[1]:
          image_dict['image_link'] = S3_PREFIX + pair[1].__str__()
        else:
          image_dict['image_link'] = False
        image_title_pairs.append(image_dict)
    return image_title_pairs

# Django Imports
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .models import Post, SacredJourney, SpiritualDirection, MinisterialRecord, MinistryPage, MainPage, GuidedMeditation, GuidedMeditationPage, GalleryImage, SlideImage, Music, StyleControl

from .forms import SacredJourneyForm, SlideImageForm, GalleryImageUpdateForm, StyleControlForm

def art_and_music(request):
  style_control = StyleControl.objects.first()
  songs = Music.objects.order_by('-created_on')
  image_dict = {}
  for cat in GalleryImage.CATEGORY_CHOICES:
    image_dict[cat[1]] = {
      'image': GalleryImage.objects.filter(category=cat[0]).order_by('-created_on').first(),
      'heading': cat[1],
    }
  return render(
    request, 'art-and-music/index.html', {
      'image_dict': image_dict,
      'songs': songs,
      'style_control': style_control,
      }
    )

class MusicCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'main_app.add_music'
  model = Music
  fields = '__all__'
  success_url = '/art-and-music/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class MusicDelete(PermissionRequiredMixin, DeleteView):
  permission_required = 'main_app.delete_music'
  model = Music
  fields = '__all__'
  success_url = '/art-and-music/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class MusicUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_music'
  model = Music
  fields = ['title', 'description']
  template_name = 'main_app/music_form.html'
  success_url = '/art-and-music/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class GalleryImageCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'main_app.add_galleryimage'
  model = GalleryImage
  fields = '__all__'
  success_url = '/art-and-music/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class GalleryImageDelete(PermissionRequiredMixin, DeleteView):
  permission_required = 'main_app.delete_galleryimage'
  model = GalleryImage
  fields = '__all__'
  success_url = '/art-and-music/'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

def photos_category(request, url_cat):
  style_control = StyleControl.objects.first()
  for cat in GalleryImage.CATEGORY_CHOICES:
    if cat[1].lower().replace(' ', '-') == url_cat:
      display = GalleryImage.objects.filter(category=cat[0]).order_by('-created_on')
      title = cat[1]
      for dis in display:
        print(dis.get_absolute_url())
  return render(request, 'art-and-music/photo-cat.html', {
    'display': display,
    'title': title,
    'style_control': style_control,
    })

class GalleryImageUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_galleryimage'
  model = GalleryImage
  form_class = GalleryImageUpdateForm
  template_name = 'main_app/galleryimageupdate_form.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

def ministry(request):
  ministry_page = MinistryPage.objects.first()
  style_control = StyleControl.objects.first()
  return render(request, 'ministry.html', {
    'ministry_page': ministry_page,
    'style_control': style_control
    })

def ministerial_record(request):
  min_rec = MinisterialRecord.objects.first()
  style_control = StyleControl.objects.first()
  menu_images = make_menu_strings(min_rec)
  return render(request, 'ministerial-record.html', {
    'min_rec': min_rec,
    'menu_images': menu_images,
    'style_control': style_control
    })

class MinisterialRecordUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'ministerial_record.update_ministerial_records'
  model = MinisterialRecord
  fields = '__all__'
  success_url = '/ministry/ministerial-record/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

### Sacred Journeys ###
def sacred_journeys_index(request):
  style_control = StyleControl.objects.first()
  journeys = SacredJourney.objects.filter(status=1).order_by('-end_date')
  today = date.today()
  upcoming_journeys = []
  previous_journeys = []
  for journey in journeys:
    if journey.start_date > today:
      upcoming_journeys.append(journey)
    else:
      previous_journeys.append(journey)
  return render(
    request,
    'sacred-journeys/index.html', {
      'upcoming_journeys': upcoming_journeys,
      'previous_journeys': previous_journeys,
      'style_control': style_control,
    },
    )

class SacredJourneyDetail(generic.DetailView):
  model = SacredJourney
  template_name = 'sacred-journeys/detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class SacredJourneyCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'sacred_journey.add_sacred_journeys'
  model = SacredJourney
  form_class = SacredJourneyForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class SacredJourneyUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'sacred_journey.update_sacred_journeys'
  model = SacredJourney
  form_class = SacredJourneyForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class SacredJourneyDelete(PermissionRequiredMixin, DeleteView):
  permission_required = 'sacred_journey.delete_sacred_journey'
  model = SacredJourney
  success_url = '/sacred-journeys/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

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
  spi_dir = SpiritualDirection.objects.first()
  style_control = StyleControl.objects.first()
  menu_images = make_menu_strings(spi_dir)
  return render(request, 'spiritual-direction.html', {
    'spi_dir': spi_dir,
    'menu_images': menu_images,
    'style_control': style_control
    })

class SpiritualDirectionUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'sacred_journey.update_spiritual_directions'
  model = SpiritualDirection
  fields = '__all__'
  success_url = '/spiritual-direction/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

#### Home #####
def home(request):
  main_page = MainPage.objects.first()
  style_control = StyleControl.objects.first()
  print(style_control.get_font_family_display)
  slide_image_form = SlideImageForm
  menu_images = make_menu_strings(main_page)
  num_visits = request.session.get('num_visits', 0)
  request.session['num_visits'] = num_visits + 1
  slide_images = main_page.slideimage_set.order_by('order')
  return render(request, 'index.html', {
    'menu_images': menu_images,
    'main_page': main_page,
    'slide_image_form': slide_image_form,
    'slide_images': slide_images,
    'style_control': style_control,
    })

class MainPageUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_mainpage'
  model = MainPage
  fields = '__all__'
  success_url = '/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class StyleControlUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_stylecontrol'
  model = StyleControl
  # fields = '__all__'
  form_class = StyleControlForm
  success_url = '/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

def edit_slides(request, main_page_id):
  style_control = StyleControl.objects.first()
  main_page = MainPage.objects.get(id=main_page_id)
  slide_image_form = SlideImageForm
  slide_images = main_page.slideimage_set.order_by('order')
  return render(request, 'main_app/slideimage_forms.html', {
    'main_page': main_page,
    'slide_image_form': slide_image_form,
    'slide_images': slide_images,
    'style_control': style_control,
  })

def add_slide_image(request, main_page_id):
  form = SlideImageForm(request.POST, request.FILES)
  if form.is_valid() and request.FILES['image']:
    new_slide_image = form.save(commit=False)
    new_slide_image.main_page_id = main_page_id
    new_slide_image.save()
  return redirect('home')

class SlideImageDelete(PermissionRequiredMixin, DeleteView):
  permission_required = 'main_app.delete_slideimage'
  model = SlideImage
  success_url = '/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

#### Blog #####
class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'blog/index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

def posts_index(request):
  posts = Post.objects.filter(status=1).order_by('-created_on')
  style_control = StyleControl.objects.first()
  return render(request, 'blog/index.html', {
    'posts': posts,
    'style_control': style_control,
    })

class PostDetail(generic.DetailView):
  model = Post
  template_name = 'blog/post_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class PostCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'main_app.add_post'
  model = Post
  fields = ['title', 'content', 'status', 'image']

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class PostUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'post.update_posts'
  model = Post
  fields = ['title', 'content', 'status', 'image']

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class PostDelete(PermissionRequiredMixin, DeleteView):
  permission_required = 'post.delete_posts'
  model = Post
  success_url = '/blog/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

#### Guided Meditations ####
class GuidedMeditationList(generic.ListView):
  model = GuidedMeditation
  ueryset = GuidedMeditation.objects.order_by('-created_on')
  template_name = 'guided-meditations.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_info'] = GuidedMeditationPage.objects.first()
    context['style_control'] = StyleControl.objects.first()
    return context

class GuidedMeditationCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'main_app.add_guidedmeditation'
  model = GuidedMeditation
  fields = '__all__'
  success_url = '/guided-meditations/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class GuidedMeditationUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_guidedmeditation'
  model = GuidedMeditation
  fields = '__all__'
  success_url = '/guided-meditations/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class GuidedMeditationDelete(PermissionRequiredMixin, DeleteView):
  permission_required = 'main_app.delete_guidedmeditation'
  model = GuidedMeditation
  success_url = '/guided-meditations/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context

class GuidedMeditationPageUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_guidedmeditationpage'
  model = GuidedMeditationPage
  fields = '__all__'
  success_url = '/guided-meditations/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context
    
def google_site_verification(request):
  return render(request, 'google2968686464ca0744.html')