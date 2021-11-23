import re

from django.db import models
from django.contrib.auth.models import User

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

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return self.title

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
  PREFIX = 'https://docs.google.com/uc?export=download&id='
  SUFFIX = '&export=download'

  title = models.CharField(max_length=200, unique=True)
  source = models.URLField(blank=True)
  description = models.CharField(max_length=250, blank=True)
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
    return self.PREFIX + self.get_source_id()

  @property
  def download_link(self):
    return self.PREFIX + self.get_source_id() + self.SUFFIX
  
