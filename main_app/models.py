# Python Imports
from urllib import request as ulreq
from PIL import Image, ImageOps
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

MEDIA_PREFIX = 'https://revwaynew.s3.amazonaws.com/'

STATUS = (
  (0, "Draft"),
  (1, "Publish")
)

# helper function
def get_sizes(uri):
  file = ulreq.urlopen(uri)
  im = Image.open(file)
  transposed_im = ImageOps.exif_transpose(im)
  file.close()
  if transposed_im.size:
    return transposed_im.size

class StyleControl(models.Model):
  global_style = models.TextField(blank=True, null=True)
  font_color = models.CharField(max_length=200, blank=True, null=True)
  background_color = models.CharField(max_length=200, blank=True, null=True)
  font_family = models.CharField(max_length=200, blank=True, null=True)
  font_weight = models.CharField(max_length=200, blank=True, null=True)

class Post(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts', default='revwayne')
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  status = models.IntegerField(choices=STATUS, default=0)
  image = models.FileField(upload_to='media/', blank=True, null=True)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('post_detail', kwargs={'slug': self.slug})
  
  @property
  def image_link(self):
    return MEDIA_PREFIX + self.image.__str__()

class Music(models.Model):
  title = models.CharField(max_length=200, unique=True)
  audio_file = models.FileField(upload_to='media/meditations/')
  description = models.CharField(max_length=255, blank=True, null=True)
  updated_on = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.title

  @property
  def audio_link(self):
    return MEDIA_PREFIX + self.audio_file.__str__()
    
class MinistryPage(models.Model):
  heading = models.CharField(max_length=20, default='Ministry')
  video_link = models.URLField(blank=True, null=True)
  video_caption = models.TextField(blank=True, null=True)
  other_text = models.TextField(blank=True, null=True)
  created_on = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['created_on']

  def __str__(self):
    return self.heading

class MinisterialRecord(models.Model):
  record_pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)
  preaching_worship_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  pastoral_care_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  spiritual_life_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  community_connection_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  religious_education_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  administration_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  first_name = models.CharField(max_length=20, blank=True, null=True)
  middle_initial = models.CharField(max_length=1, blank=True, null=True)
  last_name = models.CharField(max_length=20, blank=True, null=True)
  mailing_address = models.CharField(max_length=100, blank=True, null=True)
  city = models.CharField(max_length=20, blank=True, null=True)
  state_prov = models.CharField(max_length=20, blank=True, null=True)
  postal_zip = models.CharField(max_length=10, blank=True, null=True)
  email = models.CharField(max_length=100, blank=True, null=True)
  website = models.CharField(max_length=50, blank=True, null=True)
  phone_home = models.CharField(max_length=20, blank=True, null=True)
  phone_office = models.CharField(max_length=20, blank=True, null=True)
  phone_mobile = models.CharField(max_length=20, blank=True, null=True)
  present_position = models.CharField(max_length=50, blank=True, null=True)
  present_position_startdate = models.DateField(blank=True, null=True)
  preliminary_uu_fellowship_startdate = models.DateField(blank=True, null=True)
  why_are_you_seeking_a_ministry_now = models.TextField(blank=True, null=True)
  describe_the_new_ministry_you_hope_for = models.TextField(blank=True, null=True)
  awards_and_honors = models.TextField(blank=True, null=True)
  published_writings = models.TextField(blank=True, null=True)
  personal_and_family_situation = models.TextField(blank=True, null=True)
  background_and_development = models.TextField(blank=True, null=True)
  denominational_and_community_activities = models.TextField(blank=True, null=True)
  nonprofessional_interests = models.TextField(blank=True, null=True)
  ministerial_development = models.TextField(blank=True, null=True)
  ministerial_roles_and_functions = models.TextField(blank=True, null=True)
  ministerial_skills_and_current_special_interests = models.TextField(blank=True, null=True)
  approach_to_religious_education = models.TextField(blank=True, null=True)
  role_of_music_and_arts = models.TextField(blank=True, null=True)
  involvement_in_stewardship = models.TextField(blank=True, null=True)
  theological_orientation = models.TextField(blank=True, null=True)
  preaching_worship = models.TextField(blank=True, null=True)
  pastoral_care = models.TextField(blank=True, null=True)
  spiritual_life = models.TextField(blank=True, null=True)
  community_connection = models.TextField(blank=True, null=True)
  religious_education = models.TextField(blank=True, null=True)
  administration = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.first_name

  def get_fields(self):
    return [(field.name, getattr(self, field.name)) for field in MinisterialRecord._meta.fields]
  
  @property
  def pdf_link(self):
    return MEDIA_PREFIX + self.record_pdf.__str__()

class GuidedMeditationPage(models.Model):
  title = models.CharField(max_length=200, unique=True)
  main_text = models.TextField(blank=True, null=True)
  main_image = models.FileField(upload_to='media/meditations/', blank=True, null=True)
  
  def __str__(self):
    return str(self.id)

  @property
  def image_link(self):
    return MEDIA_PREFIX + self.main_image.__str__()

class GuidedMeditation(models.Model):
  title = models.CharField(max_length=200, unique=True)
  audio_file = models.FileField(upload_to='media/meditations/')
  description = models.CharField(max_length=255, blank=True, null=True)
  updated_on = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.title

  @property
  def audio_link(self):
    return MEDIA_PREFIX + self.audio_file.__str__()

class GalleryImage(models.Model):
  PEOPLE = 'PE'
  PLACES = 'PL'
  MYSTICAL_MOMENTS = 'MM'
  NATURE = 'NA'
  CATEGORY_CHOICES = [
    (PEOPLE, 'People'),
    (PLACES, 'Places'),
    (MYSTICAL_MOMENTS, 'Mystical Moments'),
    (NATURE, 'Nature'),
  ]

  category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
  caption = models.CharField(max_length=250, blank=True, null=True)
  font_size = models.CharField(max_length=200, null=True, blank=True)
  image = models.FileField(upload_to='media/gallery-images/', blank=True, null=True)
  updated_on = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return str(self.id)

  @property
  def image_link(self):
    return MEDIA_PREFIX + self.image.__str__()

  @property
  def image_type(self):
    width, height = get_sizes(self.image_link)
    if width > height:
      return 'landscape'
    else:
      return 'portrait'

class MainPage(models.Model):
  tagline = models.TextField(blank=True, null=True)
  main_text = models.TextField(blank=True, null=True)
  blog_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  spiritual_direction_image = models.FileField(upload_to='media/main-menu-images/', blank=True, null=True)
  guided_meditations_image = models.FileField(upload_to='media/main-menu-images/', blank=True, null=True)
  sacred_journeys_image = models.FileField(upload_to='media/main-menu-images/', blank=True, null=True)
  ministry_image = models.FileField(upload_to='media/main-menu-images/', blank=True, null=True)
  art_and_music_image = models.FileField(upload_to='media/main-menu-images/', blank=True, null=True)

  def __str__(self):
    return str(self.id)
  
  def get_fields(self):
    return [(field.name, getattr(self, field.name)) for field in MainPage._meta.fields]

class SlideImage(models.Model):
  order = models.PositiveIntegerField(blank=True, null=True)
  image = models.FileField(upload_to='media/slideshow/')
  main_page = models.ForeignKey(MainPage, on_delete=models.CASCADE)

  def __str__(self):
    return 'Slide Image #' + str(self.id)

  @property
  def image_link(self):
    return MEDIA_PREFIX + self.image.__str__()
  
class SacredJourney(models.Model):
  image = models.FileField(upload_to='media/', blank=True, null=True)
  name = models.CharField(max_length=200, unique=True)
  start_date = models.DateField()
  end_date = models.DateField()
  destination = models.CharField(max_length=50)
  worldwidequest_link = models.URLField(blank=True, null=True)
  description = models.TextField()
  itinerary = models.TextField(blank=True, null=True)
  tour_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  group_size = models.IntegerField(blank=True, null=True)
  map_image = models.URLField(blank=True, null=True)
  included_features = models.TextField(blank=True, null=True)
  updated_on = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=0)
  slug = models.SlugField(max_length=200, unique=True)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('sacred_journey_detail', kwargs={'slug': self.slug})

  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.name)
    super(SacredJourney, self).save(*args, **kwargs)

  @property
  def image_link(self):
    return MEDIA_PREFIX + self.image.__str__()

class SpiritualDirection(models.Model):
  title = models.TextField(blank=True, null=True, default='Spiritual Direction')
  blurb = models.TextField(max_length=400, blank=True, null=True)
  what_is_spiritual_direction_image = models.FileField(upload_to='media/spiritual-direction-images/', blank=True, null=True)
  what_do_spiritual_directors_do_image = models.FileField(upload_to='media/spiritual-direction-images/', blank=True, null=True)
  one_on_one_sessions_image = models.FileField(upload_to='media/spiritual-direction-images/', blank=True, null=True)
  contact_wayne_for_a_session_image = models.FileField(upload_to='media/spiritual-direction-images/', blank=True, null=True)
  what_is_spiritual_direction = models.TextField(blank=True, null=True)
  what_do_spiritual_directors_do = models.TextField(blank=True, null=True)
  one_on_one_sessions = models.TextField(blank=True, null=True)
  contact_wayne_for_a_session = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.title

  def get_fields(self):
    return [(field.name, getattr(self, field.name)) for field in SpiritualDirection._meta.fields]