# Python Imports
import re

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify
from django.urls import reverse

PREFIX = 'https://docs.google.com/uc?export=download&id='
SUFFIX = '&export=download'
PHOTO_PREFIX = 'https://docs.google.com/uc?export=view&id='

MEDIA_PREFIX = 'https://revwaynew.s3.amazonaws.com/'

STATUS = (
  (0, "Draft"),
  (1, "Publish")
)

class Post(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts', default='revwayne')
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  status = models.IntegerField(choices=STATUS, default=0)
  image_source = models.URLField(blank=True, null=True)
  image = models.FileField(upload_to='media/', blank=True, null=True)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)

  def get_image_source_id(self):
    image_source_id = re.search('/d/(.+?)/view', self.image_source).group(1)
    return image_source_id

  def get_absolute_url(self):
    return reverse('post_detail', kwargs={'slug': self.slug})

  @property
  def photo_link(self):
    return PHOTO_PREFIX + self.get_image_source_id()
  
  @property
  def image_link(self):
    return MEDIA_PREFIX + self.image.__str__()

class MainPageFragment(models.Model):
  role = models.CharField(max_length=20, unique=True)
  content = models.TextField()
  created_on = models.DateTimeField(auto_now=True)

  class Meta: 
    ordering = ['created_on']

  def __str__(self):
    return self.role

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

class MinisterialRecordImage(models.Model):
  PREACHING_WORSHIP = 'PW'
  PASTORAL_CARE = 'PC'
  SPIRITUAL_LIFE = 'SL'
  COMMUNITY_CONNECTION = 'CC'
  RELIGIOUS_EDUCATION = 'RE'
  ADMINISTRATION = 'AD'
  CATEGORY_CHOICES = [
    (PREACHING_WORSHIP, 'PW'),
    (PASTORAL_CARE, 'PC'),
    (SPIRITUAL_LIFE, 'SL'),
    (COMMUNITY_CONNECTION, 'CC'),
    (RELIGIOUS_EDUCATION, 'RE'),
    (ADMINISTRATION, 'AD')
  ]

  name_of_file = models.CharField(max_length=200, unique=True)
  category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
  source = models.URLField()
  updated_on = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now=True)
  position = models.PositiveIntegerField(
    unique=True,
    blank=True,
    null=True,
    validators=[
      MaxValueValidator(6),
      MinValueValidator(1)
    ])

  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.name_of_file

  def get_source_id(self):
    source_id = re.search('/d/(.+?)/view', self.source).group(1)
    return source_id

  @property
  def photo_link(self):
    return PHOTO_PREFIX + self.get_source_id()

class MinisterialRecord(models.Model):
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
  preaching_worship_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  pastoral_care_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  spiritual_life_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  community_connection_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  religious_education_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  administration_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)

  def __str__(self):
    return self.first_name

  @property
  def pw_image_link(self):
    return MEDIA_PREFIX + self.preaching_worship_image.__str__()

  @property
  def pc_image_link(self):
    return MEDIA_PREFIX + self.pastoral_care_image.__str__()
  
  @property
  def sl_image_link(self):
    return MEDIA_PREFIX + self.spiritual_life_image.__str__()

  @property
  def cc_image_link(self):
    return MEDIA_PREFIX + self.community_connection_image.__str__()

  @property
  def re_image_link(self):
    return MEDIA_PREFIX + self.religious_education_image.__str__()

  @property
  def a_image_link(self):
    return MEDIA_PREFIX + self.administration_image.__str__()

class Meditation(models.Model):
  title = models.CharField(max_length=200, unique=True)
  source = models.URLField(blank=True, null=True)
  description = models.CharField(max_length=250, blank=True, null=True)
  updated_on = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=0)

  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.title

  def get_source_id(self):
    source_id = re.search('/d/(.+?)/view', self.source).group(1)
    return source_id

  @property
  def audio_link(self):
    return PREFIX + self.get_source_id()

  @property
  def download_link(self):
    return PREFIX + self.get_source_id() + SUFFIX

class Photo(models.Model):
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

  name_of_file = models.CharField(max_length=200, unique=True)
  category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, blank=True, null=True)
  source = models.URLField(blank=True, null=True)
  description = models.CharField(max_length=250, blank=True, null=True)
  updated_on = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.name_of_file

  def get_source_id(self):
    source_id = re.search('/d/(.+?)/view', self.source).group(1)
    return source_id

  @property
  def photo_link(self):
    return PHOTO_PREFIX + self.get_source_id()

class MainPagePhoto(models.Model):
  SLIDESHOW_IMAGE = 'SI'
  MENU_IMAGE = 'MI'
  ROLE_CHOICES = [
    (SLIDESHOW_IMAGE, 'Slideshow'),
    (MENU_IMAGE, 'Menu')
  ]

  SPIRITUAL_DIRECTION = 'SD'
  BLOG = 'BL'
  GUIDED_MEDITATIONS = 'GM'
  SACRED_JOURNEYS = 'SJ'
  MINISTRY = 'MY'
  ART_AND_MUSIC = 'AM'
  HYPERLINK_CHOICES = [
    (SPIRITUAL_DIRECTION, 'spiritual_direction'),
    (BLOG, 'blog'),
    (GUIDED_MEDITATIONS, 'guided_meditations'),
    (MINISTRY, 'ministry'),
    (SACRED_JOURNEYS, 'sacred_journeys'),
    (ART_AND_MUSIC, 'art_and_music'),
  ]

  role = models.CharField(max_length=2, choices=ROLE_CHOICES)
  status = models.IntegerField(choices=STATUS, default=0)
  order = models.PositiveIntegerField()
  photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
  hyperlink = models.CharField(max_length=2, choices=HYPERLINK_CHOICES, blank=True, null=True)

  def __str__(self):
    return self.photo.name_of_file
  
class SacredJourney(models.Model):
  name = models.CharField(max_length=200, unique=True)
  start_date = models.DateField()
  end_date = models.DateField()
  destination = models.CharField(max_length=50)
  banner_picture = models.URLField(blank=True, null=True)
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
