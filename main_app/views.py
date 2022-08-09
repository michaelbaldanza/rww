# Python Imports
import re, warnings
from datetime import date

S3_PREFIX = 'https://revwaynew.s3.amazonaws.com/'

# Helper function
def make_menu_strings(record, *argv):
  if record:
    image_title_pairs = []
    for pair in record.get_fields():
      if '_image' in pair[0] :
        image_dict = {
          'text': pair[0].replace('_', ' ').replace(' image', ''),
        }
        if pair[1]:
          image_dict['image_link'] = S3_PREFIX + pair[1].__str__()
        else:
          image_dict['image_link'] = False
        image_title_pairs.append(image_dict)
    return image_title_pairs

def select_fields(some_model, *selected_fields):
  model_fields = some_model._meta.get_fields()
  field_list = []
  for field in model_fields:
    for selected in selected_fields:
      if field.name.startswith(selected):
        field_list.append(field.name)
  return field_list

def make_labels(field_list, **custom_labels):
  label_dict = {}
  for key, value in custom_labels.items():
    for item in field_list:
      if item.startswith(key):
        spaced_string = item.replace(key, value).replace('_', ' ')
        label_dict[item] = spaced_string.capitalize()
  return label_dict


def on_load(req):
  print(req)

# Django Imports
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import (LoginRequiredMixin,
  UserPassesTestMixin, PermissionRequiredMixin)
from .models import (Post, SacredJourney, SpiritualDirection,
  MinisterialRecord, MinistryPage, MainPage, GuidedMeditation,
  GuidedMeditationPage, GalleryImage, SlideImage, Music, StyleControl,
  ArtAndMusicPage, SacredJourneyPage, BlogIndexPage, GlobalPostStyle,
  StyleSheet, ContactPage)

from .forms import (SacredJourneyForm, SlideImageForm, GalleryImageUpdateForm,
  StyleControlForm, BlogIndexPageForm, PostForm, MainPageForm, StyleSheetForm,
  MainPageStyleSheetForm, PostStyleSheetForm, SpiritualDirectionForm,
  SpiritualDirectionStyleSheetForm, MinisterialRecordForm,
  MinisterialRecordStyleSheetForm, ArtAndMusicPageForm,
  ArtAndMusicPageStyleSheetForm, SacredJourneyStyleSheetForm,
  GuidedMeditationPageForm, GuidedMeditationPageStyleSheetForm,
  GalleryImageStyleSheetForm, GalleryImageCreateForm, ContactPageForm,
  ContactPageStyleSheetForm, BlogIndexPageForm, BlogIndexPageStyleSheetForm,
  SacredJourneyPageForm, SacredJourneyPageStyleSheetForm)

def admin_check(user):
  print('hitting admin_check')
  return user.is_staff

def art_and_music(request):
  style_control = StyleControl.objects.first()
  songs = Music.objects.order_by('-created_on')
  page = ArtAndMusicPage.objects.first()
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
      'page': page,
      }
    )

class ArtAndMusicPageUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_artandmusicpage'
  model = ArtAndMusicPage
  second_model = StyleSheet
  form_class = ArtAndMusicPageForm
  second_form_class = ArtAndMusicPageStyleSheetForm
  success_url = '/art-and-music/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    page = self.object
    style = self.second_model.objects.get(id=page.style_sheet.id)
    if 'form' not in context:
      context['form'] = self.form_class(instance=page)
    if 'form2' not in context:
      context['form2'] = self.second_form_class(instance=style)
    context['style_control'] = StyleControl.objects.first()
    return context

  def post(self, request, *args, **kwargs):
    page = self.model.objects.get(id=kwargs['pk'])
    style = self.second_model.objects.get(id=page.style_sheet.id)
    form = self.form_class(request.POST, instance=page)
    form2 = self.second_form_class(request.POST, instance=style)
    if form.is_valid() and form2.is_valid():
      form.save()
      form2.save()
    return redirect('art_and_music')

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
  form_class = GalleryImageCreateForm
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
        print(dis.style_sheet)
        print(dis.get_absolute_url())
  return render(request, 'art-and-music/photo-cat.html', {
    'display': display,
    'title': title,
    'style_control': style_control,
    })

class GalleryImageUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_galleryimage'
  model = GalleryImage
  second_model = StyleSheet
  form_class = GalleryImageUpdateForm
  second_form_class = GalleryImageStyleSheetForm
  # template_name = 'main_app/galleryimageupdate_form.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    page = self.object
    style = self.second_model.objects.get(id=page.style_sheet.id)
    if 'form' not in context:
      context['form'] = self.form_class(instance=page)
    if 'form2' not in context:
      context['form2'] = self.second_form_class(instance=style)
    context['style_control'] = StyleControl.objects.first()
    return context

  def post(self, request, *args, **kwargs):
    page = self.model.objects.get(id=kwargs['pk'])
    style = self.second_model.objects.get(id=page.style_sheet.id)
    form = self.form_class(request.POST, instance=page)
    form2 = self.second_form_class(request.POST, instance=style)
    if form.is_valid() and form2.is_valid():
      form.save()
      form2.save()
    return redirect('art_and_music')

def ministry(request):
  ministry_page = MinistryPage.objects.first()
  style_control = StyleControl.objects.first()
  return render(request, 'ministry.html', {
    'ministry_page': ministry_page,
    'style_control': style_control
    })

def ministerial_record(request):
  page = MinisterialRecord.objects.first()
  style_control = StyleControl.objects.first()
  menu_images = make_menu_strings(page)
  return render(request, 'ministerial-record.html', {
    'page': page,
    'menu_images': menu_images,
    'style_control': style_control
    })

class MinisterialRecordUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'ministerial_record.update_ministerial_records'
  model = MinisterialRecord
  second_model = StyleSheet
  form_class = MinisterialRecordForm
  second_form_class = MinisterialRecordStyleSheetForm
  success_url = '/ministry/ministerial-record/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    page = self.object
    style = self.second_model.objects.get(id=page.style_sheet.id)
    if 'form' not in context:
      context['form'] = self.form_class(instance=page)
    if 'form2' not in context:
      context['form2'] = self.second_form_class(instance=style)
    context['style_control'] = StyleControl.objects.first()
    return context

  def post(self, request, *args, **kwargs):
    page = self.model.objects.get(id=kwargs['pk'])
    style = self.second_model.objects.get(id=page.style_sheet.id)
    form = self.form_class(request.POST, request.FILES, instance=page)
    form2 = self.second_form_class(request.POST, instance=style)
    if form.is_valid() and form2.is_valid():
      form.save()
      form2.save()
    return redirect('ministerial_record')

### Sacred Journeys ###
def sacred_journeys_index(request):
  style_control = StyleControl.objects.first()
  page = SacredJourneyPage.objects.first()
  journeys = SacredJourney.objects.filter(status=1).order_by('-end_date')
  today = date.today()
  upcoming_journeys = []
  previous_journeys = []
  for journey in journeys:
    print('theres a journey')
    if journey.start_date > today:
      print(journey)
      upcoming_journeys.append(journey)
    else:
      print('previous journey')
      previous_journeys.append(journey)
  return render(
    request,
    'sacred-journeys/index.html', {
      'upcoming_journeys': upcoming_journeys,
      'previous_journeys': previous_journeys,
      'style_control': style_control,
      'page': page,
    },
    )

class SacredJourneyPageUpdate(generic.UpdateView):
  permission_required = 'main_app.change_sacredjourneypage'
  model = SacredJourneyPage
  second_model = StyleSheet
  form_class = SacredJourneyPageForm
  second_form_class = SacredJourneyPageStyleSheetForm
  success_url = '/sacred-journeys/'

  def get_context_data(self, **kwargs):
    # context = super(MainPageUpdate, self).get_context_data(**kwargs)
    context = super().get_context_data(**kwargs)
    page = self.object
    style = self.second_model.objects.get(id=page.style_sheet.id)
    if 'form' not in context:
      context['form'] = self.form_class(instance=page)
    if 'form2' not in context:
      context['form2'] = self.second_form_class(instance=style)
    context['style_control'] = StyleControl.objects.first()
    return context

  def post(self, request, *args, **kwargs):
    page = self.model.objects.get(id=kwargs['pk'])
    style = self.second_model.objects.get(id=page.style_sheet.id)
    form = self.form_class(request.POST, request.FILES, instance=page)
    form2 = self.second_form_class(request.POST, instance=style)
    if form.is_valid() and form2.is_valid():
      form.save()
      form2.save()
    return redirect('sacred_journeys')

class SacredJourneyDetail(generic.DetailView):
  model = SacredJourney
  template_name = 'sacred-journeys/detail.html'

  def get_context_data(self, **kwargs):
    journey = super().get_object()
    context = super().get_context_data(**kwargs)
    context['page'] = journey
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
  second_model = StyleSheet
  form_class = SacredJourneyForm
  second_form_class = SacredJourneyStyleSheetForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    page = self.object
    style = self.second_model.objects.get(id=page.style_sheet.id)
    if 'form' not in context:
      context['form'] = self.form_class(instance=page)
    if 'form2' not in context:
      context['form2'] = self.second_form_class(instance=style)
    context['style_control'] = StyleControl.objects.first()
    return context

  def post(self, request, *args, **kwargs):
    page = self.model.objects.get(slug=kwargs['slug'])
    style = self.second_model.objects.get(id=page.style_sheet.id)
    form = self.form_class(request.POST, request.FILES, instance=page)
    form2 = self.second_form_class(request.POST, instance=style)
    if form.is_valid() and form2.is_valid():
      form.save()
      form2.save()
    return HttpResponseRedirect(reverse('sacred_journey_detail', kwargs={'slug': page.slug}))

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
  page = SpiritualDirection.objects.first()
  style_control = StyleControl.objects.first()
  menu_images = make_menu_strings(page)
  return render(request, 'spiritual-direction.html', {
    'page': page,
    'menu_images': menu_images,
    'style_control': style_control
    })

class SpiritualDirectionUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_spiritualdirection'
  model = SpiritualDirection
  second_model = StyleSheet
  form_class = SpiritualDirectionForm
  second_form_class = SpiritualDirectionStyleSheetForm
  success_url = '/spiritual-direction/'

  def get_context_data(self, **kwargs):
    # context = super(SpiritualDirectionUpdate, self).get_context_data(**kwargs)
    context = super().get_context_data(**kwargs)
    print(context)
    page = self.object
    print('printing self.form_class')
    print(self.form_class)
    style = self.second_model.objects.get(id=page.style_sheet.id)
    if 'form' not in context:
      context['form'] = self.form_class(instance=page)
    if 'form2' not in context:
      context['form2'] = self.second_form_class(instance=style)
    context['style_control'] = StyleControl.objects.first()
    return context

  def post(self, request, *args, **kwargs):
    page = self.model.objects.get(id=kwargs['pk'])
    style = self.second_model.objects.get(id=page.style_sheet.id)
    form = self.form_class(request.POST, request.FILES, instance=page)
    form2 = self.second_form_class(request.POST, instance=style)
    if form.is_valid() and form2.is_valid():
      form.save()
      form2.save()
    return redirect('spiritual_direction')



#### Home #####
def home(request):
  page = MainPage.objects.first()
  style_control = StyleControl.objects.first()
  # print('this is the path')
  # on_load(request.path_info)
  slide_image_form = SlideImageForm
  menu_images = make_menu_strings(page)
  num_visits = request.session.get('num_visits', 0)
  request.session['num_visits'] = num_visits + 1
  slide_images = page.slideimage_set.order_by('order')
  return render(request, 'index.html', {
    'menu_images': menu_images,
    'page': page,
    'slide_image_form': slide_image_form,
    'slide_images': slide_images,
    'style_control': style_control,
    })

class MainPageUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_mainpage'
  model = MainPage
  second_model = StyleSheet
  form_class = MainPageForm
  second_form_class = MainPageStyleSheetForm
  success_url = '/'

  def get_context_data(self, **kwargs):
    # context = super(MainPageUpdate, self).get_context_data(**kwargs)
    context = super().get_context_data(**kwargs)
    page = self.object
    style = self.second_model.objects.get(id=page.style_sheet.id)
    if 'form' not in context:
      context['form'] = self.form_class(instance=page)
    if 'form2' not in context:
      context['form2'] = self.second_form_class(instance=style)
    context['style_control'] = StyleControl.objects.first()
    return context

  def post(self, request, *args, **kwargs):
    page = self.model.objects.get(id=kwargs['pk'])
    style = self.second_model.objects.get(id=page.style_sheet.id)
    form = self.form_class(request.POST, request.FILES, instance=page)
    form2 = self.second_form_class(request.POST, instance=style)
    if form.is_valid() and form2.is_valid():
      form.save()
      form2.save()
    return redirect('home')

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

@user_passes_test(admin_check)
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

@user_passes_test(admin_check)
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

  def dispatch(self, request, *args, **kwargs):
        return super(PostList, self).dispatch(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    context['page'] = BlogIndexPage.objects.first()
    return context

def posts_index(request):
  page = BlogIndexPage.objects.first()
  posts = Post.objects.filter(status=1).order_by('-created_on')
  style_control = StyleControl.objects.first()
  return render(request, 'blog/index.html', {
    'page': page,
    'posts': posts,
    'style_control': style_control,
    })

class BlogIndexPageUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_mainpage'
  model = BlogIndexPage
  second_model = StyleSheet
  form_class = BlogIndexPageForm
  second_form_class = BlogIndexPageStyleSheetForm
  success_url = '/blog/'

  def get_context_data(self, **kwargs):
    # context = super(MainPageUpdate, self).get_context_data(**kwargs)
    context = super().get_context_data(**kwargs)
    page = self.object
    style = self.second_model.objects.get(id=page.style_sheet.id)
    if 'form' not in context:
      context['form'] = self.form_class(instance=page)
    if 'form2' not in context:
      context['form2'] = self.second_form_class(instance=style)
    context['style_control'] = StyleControl.objects.first()
    return context

  def post(self, request, *args, **kwargs):
    page = self.model.objects.get(id=kwargs['pk'])
    style = self.second_model.objects.get(id=page.style_sheet.id)
    form = self.form_class(request.POST, request.FILES, instance=page)
    form2 = self.second_form_class(request.POST, instance=style)
    if form.is_valid() and form2.is_valid():
      form.save()
      form2.save()
    return redirect('home')

class PostDetail(generic.DetailView):
  model = Post
  template_name = 'blog/post_detail.html'

  def get_context_data(self, **kwargs):
    post = super().get_object()
    print('The post id follows:')
    print(post.id)
    all_posts = GlobalPostStyle.objects.first()
    context = super().get_context_data(**kwargs)
    tuple_list = []
    page = {}
    context['style_control'] = StyleControl.objects.first()
    context['page'] = post
    print('trying with .self')
    for all_pair in all_posts.get_fields():
      for pair in post.get_fields():
        if all_pair[0] != 'id' and all_pair[0] == pair[0]:
          if pair[1] != None:
            print('printing all_pair')
            print(pair[0])
            print(pair[1])
            tuple_list.append(pair)
            # page.update({pair[0], pair[1]})
          elif all_pair[1] != None:
            tuple_list.append(all_pair)
            print('printing all_pair')
            print(all_pair[0])
            print(all_pair[1])
            # page.update({all_pair[0], all_pair[1]})
    print(tuple_list)
    return context

class PostCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'main_app.add_post'
  model = Post
  form_class = PostForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['style_control'] = StyleControl.objects.first()
    return context
  
  # def form_valid(self, form):
  #   style_sheet = StyleSheet.objects.create()
  #   form.style_sheet = style_sheet
  #   return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'post.update_posts'
  model = Post
  second_model = StyleSheet
  form_class = PostForm
  second_form_class = PostStyleSheetForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    page = self.object
    style = self.second_model.objects.get(id=page.style_sheet.id)
    if 'form' not in context:
      context['form'] = self.form_class(instance=page)
    if 'form2' not in context:
      context['form2'] = self.second_form_class(instance=style)
    context['style_control'] = StyleControl.objects.first()
    return context

  def post(self, request, *args, **kwargs):
    page = self.model.objects.get(slug=kwargs['slug'])
    style = self.second_model.objects.get(id=page.style_sheet.id)
    form = self.form_class(request.POST, request.FILES, instance=page)
    form2 = self.second_form_class(request.POST, instance=style)
    if form.is_valid() and form2.is_valid():
      form.save()
      form2.save()
    return HttpResponseRedirect(reverse('post_detail', kwargs={'slug': page.slug}))
    # reverse('post_detail', kwargs={'slug': page.slug})

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
  queryset = GuidedMeditation.objects.order_by('title')
  template_name = 'guided-meditations.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page'] = GuidedMeditationPage.objects.first()
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
  second_model = StyleSheet
  form_class = GuidedMeditationPageForm
  second_form_class = GuidedMeditationPageStyleSheetForm
  success_url = '/guided-meditations/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    page = self.object
    style = self.second_model.objects.get(id=page.style_sheet.id)
    if 'form' not in context:
      context['form'] = self.form_class(instance=page)
    if 'form2' not in context:
      context['form2'] = self.second_form_class(instance=style)
    context['style_control'] = StyleControl.objects.first()
    return context

  def post(self, request, *args, **kwargs):
    page = self.model.objects.get(id=kwargs['pk'])
    style = self.second_model.objects.get(id=page.style_sheet.id)
    form = self.form_class(request.POST, request.FILES, instance=page)
    form2 = self.second_form_class(request.POST, instance=style)
    if form.is_valid() and form2.is_valid():
      form.save()
      form2.save()
    return redirect('guided_meditations')
    
def contact(request):
  style_control = StyleControl.objects.first()
  page = ContactPage.objects.first()
  return render(request, 'contact.html', {
    'page': page,
    'style_control': style_control,
  })

class ContactPageUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_contactpage'
  model = ContactPage
  second_model = StyleSheet
  form_class = ContactPageForm
  second_form_class = ContactPageStyleSheetForm
  success_url = '/contact/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    page = self.object
    style = self.second_model.objects.get(id=page.style_sheet.id)
    if 'form' not in context:
      context['form'] = self.form_class(instance=page)
    if 'form2' not in context:
      context['form2'] = self.second_form_class(instance=style)
    context['style_control'] = StyleControl.objects.first()
    return context

  def post(self, request, *args, **kwargs):
    page = self.model.objects.get(id=kwargs['pk'])
    style = self.second_model.objects.get(id=page.style_sheet.id)
    form = self.form_class(request.POST, request.FILES, instance=page)
    form2 = self.second_form_class(request.POST, instance=style)
    if form.is_valid() and form2.is_valid():
      form.save()
      form2.save()
    return redirect('contact')

def google_site_verification(request):
  return render(request, 'google2968686464ca0744.html')