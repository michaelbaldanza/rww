# Python Imports
import re

from django.db import models
from django.contrib.auth.models import User

PREFIX = 'https://docs.google.com/uc?export=download&id='
SUFFIX = '&export=download'
PHOTO_PREFIX = 'https://docs.google.com/uc?export=view&id='

STATUS = (
  (0, "Draft"),
  (1, "Publish")
)

class Post(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  status = models.IntegerField(choices=STATUS, default=0)
  image_source = models.URLField(blank=True, null=True)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return self.title

  def get_image_source_id(self):
    image_source_id = re.search('/d/(.+?)/view', self.image_source).group(1)
    return image_source_id

  @property
  def photo_link(self):
    return PHOTO_PREFIX + self.get_image_source_id()

class MainPageFragment(models.Model):
  role = models.CharField(max_length=20, unique=True)
  content = models.TextField()
  created_on = models.DateTimeField(auto_now=True)

  class Meta: 
    ordering = ['created_on']

  def __str__(self):
    return self.role

class MinistryFragment(models.Model):
  role = models.CharField(max_length=20, unique=True)
  content = models.TextField()
  created_on = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['created_on']

  def __str__(self):
    return self.role

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
  
