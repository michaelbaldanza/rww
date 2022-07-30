# Python Imports
import inspect
from colorfield.fields import ColorField
from urllib import request as ulreq
from PIL import Image, ImageOps
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, RegexValidator
from django.template.defaultfilters import slugify
from django.urls import reverse

MEDIA_PREFIX = 'https://revwaynew.s3.amazonaws.com/'

STATUS = (
  (0, "Draft"),
  (1, "Publish")
)

phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


# helper function
def get_sizes(uri):
  file = ulreq.urlopen(uri)
  im = Image.open(file)
  transposed_im = ImageOps.exif_transpose(im)
  file.close()
  if transposed_im.size:
    return transposed_im.size

def make_choices(*args):
  choices = []
  for arg in args:
    print(arg)
    choice_longform = [k for k, v in locals().items() if v == arg][0]
    print(choice_longform)
    choice_tuple = (arg, choice_longform)
    choices.append(choice_tuple)
  return choices



FUTURA = 'FU'
GARAMOND = 'GA'
HELVETICA = 'HE'
PAPYRUS = 'PA'
ROCKWELL = 'RO'
SOURCE_SANS_PRO = 'SO'
TIMES_NEW_ROMAN = 'TN'
VERDANA = 'VE'
FONT_FAMILY_CHOICES = [
  (FUTURA, 'Futura'),
  (GARAMOND, 'Garamond'),
  (HELVETICA, 'Helvetica'),
  (PAPYRUS, 'Papyrus'),
  (ROCKWELL, 'Rockwell'),
  (SOURCE_SANS_PRO, 'Source Sans Pro'),
  (TIMES_NEW_ROMAN, 'Times New Roman'),
  (VERDANA, 'Verdana'),
]

FONT_SIZE_CHOICES = [(i, i) for i in range(42) if i != 0 and i % 2 == 0]
OPACITY_CHOICES = [(j, j) for j in range(100)]


NORMAL = 'NO'
BOLD = 'BO'
LIGHTER = 'LI'
BOLDER = 'BE'
FONT_WEIGHT_CHOICES = [
  (NORMAL, 'normal'),
  (BOLD, 'bold'),
  (LIGHTER, 'lighter'),
  (BOLDER, 'bolder'),
]

class StyleSheet(models.Model):
  parent = models.CharField(max_length=200, default=None, blank=True, null=True)
  primary_heading_color = ColorField(blank=True, null=True)
  primary_heading_opacity = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100),])
  primary_heading_font_size = models.IntegerField(blank=True, null=True, choices=FONT_SIZE_CHOICES)
  primary_heading_font_family = models.CharField(blank=True, null=True, choices=FONT_FAMILY_CHOICES, max_length=200)
  secondary_heading_color = ColorField(blank=True, null=True)
  secondary_heading_opacity = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100),])
  secondary_heading_font_size = models.IntegerField(blank=True, null=True, choices=FONT_SIZE_CHOICES)
  secondary_heading_font_family = models.CharField(blank=True, null=True, choices=FONT_FAMILY_CHOICES, max_length=200)
  tertiary_heading_color = ColorField(blank=True, null=True)
  tertiary_heading_opacity = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100),])
  tertiary_heading_font_size = models.IntegerField(blank=True, null=True, choices=FONT_SIZE_CHOICES)
  tertiary_heading_font_family = models.CharField(blank=True, null=True, choices=FONT_FAMILY_CHOICES, max_length=200)
  image_heading_color = ColorField(blank=True, null=True)
  image_heading_opacity = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100),])
  image_heading_font_size = models.IntegerField(blank=True, null=True, choices=FONT_SIZE_CHOICES)
  image_heading_font_family = models.CharField(blank=True, null=True, choices=FONT_FAMILY_CHOICES, max_length=200)
  body_color = ColorField(blank=True, null=True)
  body_opacity = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100),])
  body_font_size = models.IntegerField(blank=True, null=True, choices=FONT_SIZE_CHOICES)
  body_font_family = models.CharField(blank=True, null=True, choices=FONT_FAMILY_CHOICES, max_length=200)
  byline_color = ColorField(blank=True, null=True)
  byline_opacity = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100),])
  byline_font_size = models.IntegerField(blank=True, null=True, choices=FONT_SIZE_CHOICES)
  byline_font_family = models.CharField(blank=True, null=True, choices=FONT_FAMILY_CHOICES, max_length=200)
  content_heading_color = ColorField(blank=True, null=True)
  content_heading_opacity = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100),])
  content_heading_font_size = models.IntegerField(blank=True, null=True, choices=FONT_SIZE_CHOICES)
  content_heading_font_family = models.CharField(blank=True, null=True, choices=FONT_FAMILY_CHOICES, max_length=200)
  content_body_color = ColorField(blank=True, null=True)
  content_body_opacity = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100),])
  content_body_font_size = models.IntegerField(blank=True, null=True, choices=FONT_SIZE_CHOICES)
  content_body_font_family = models.CharField(blank=True, null=True, choices=FONT_FAMILY_CHOICES, max_length=200)
  created_on = models.DateTimeField(blank=True, null=True, auto_now_add=True)
  updated_on = models.DateTimeField(blank=True, null=True, auto_now=True)

  def __str__(self):
    return "%s's Sheet" % self.parent

  def get_fields(self):
    return [(field.name, getattr(self, field.name)) for field in self._meta.fields]

class StyleControl(models.Model):
  background_color = ColorField(blank=True, null=True)
  font_color = ColorField(blank=True, null=True)
  opacity = models.PositiveIntegerField(verbose_name='Opacity (%)', blank=True, null=True, validators=[MaxValueValidator(100),])
  font_size = models.IntegerField(choices=FONT_SIZE_CHOICES, blank=True, null=True)
  font_family = models.CharField(max_length=200, choices=FONT_FAMILY_CHOICES, blank=True, null=True)
  font_weight = models.CharField(max_length=200, choices=FONT_WEIGHT_CHOICES, blank=True, null=True)
  header_maintext_color = ColorField(verbose_name='\"Sitting Quietly\" color', blank=True, null=True)
  header_maintext_opacity = models.PositiveIntegerField(verbose_name='\"Sitting Quietly\" opacity (%)', blank=True, null=True, validators=[MaxValueValidator(100),])
  header_maintext_font_family = models.CharField(verbose_name='\"Sitting Quietly\" font family', max_length=200, choices=FONT_FAMILY_CHOICES, blank=True, null=True)
  header_smalltext_color = ColorField(verbose_name='\"by Rev. Wayne Walder\" color', blank=True, null=True)
  header_smalltext_opacity = models.PositiveIntegerField(verbose_name='\"by Rev. Wayne Walder opacity\" (%', blank=True, null=True, validators=[MaxValueValidator(100),])
  header_smalltext_font_family = models.CharField(verbose_name='\"by Rev. Wayne Walder\" font family', max_length=200, choices=FONT_FAMILY_CHOICES, blank=True, null=True)
  image_heading_color = ColorField(blank=True, null=True)
  image_heading_opacity = models.PositiveIntegerField(verbose_name='Image heading opacity (%)', blank=True, null=True, validators=[MaxValueValidator(100),])
  image_heading_font_family = models.CharField(max_length=200, choices=FONT_FAMILY_CHOICES, blank=True, null=True)

class BlogIndexPage(models.Model):
  title = models.CharField(max_length=200, default='Blog Index')
  style_sheet = models.OneToOneField(
    StyleSheet,
    on_delete=models.CASCADE,
    null=True,
    )

  def __str__(self):
    return self.title

class GlobalPostStyle(models.Model):
  primary_heading_font_color = ColorField(verbose_name='heading color', blank=True, null=True)
  primary_heading_opacity = models.PositiveIntegerField(verbose_name='heading opacity (%)', blank=True, null=True, validators=[MaxValueValidator(100),])
  primary_heading_font_size = models.IntegerField(verbose_name='heading size (px)', choices=FONT_SIZE_CHOICES, blank=True, null=True)
  primary_heading_font_family = models.CharField(verbose_name='heading font', max_length=200, choices=FONT_FAMILY_CHOICES, blank=True, null=True)
  body_font_color = ColorField(verbose_name='body color', blank=True, null=True)
  body_opacity = models.PositiveIntegerField(verbose_name='body opacity (%)', blank=True, null=True, validators=[MaxValueValidator(100),])
  body_font_size = models.IntegerField(verbose_name='body size (px)', choices=FONT_SIZE_CHOICES, blank=True, null=True)
  body_font_family = models.CharField(verbose_name='body font', max_length=200, choices=FONT_FAMILY_CHOICES, blank=True, null=True)
  byline_font_color = ColorField(verbose_name='byline color', blank=True, null=True)
  byline_opacity = models.PositiveIntegerField(verbose_name='byline opacity (%)', blank=True, null=True, validators=[MaxValueValidator(100),])
  byline_font_size = models.IntegerField(verbose_name='byline size (px)', choices=FONT_SIZE_CHOICES, blank=True, null=True)
  byline_font_family = models.CharField(verbose_name='byline font', max_length=200, choices=FONT_FAMILY_CHOICES, blank=True, null=True)

  def get_fields(self):
    return [(field.name, getattr(self, field.name)) for field in self._meta.fields]

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

class ArtAndMusicPage(models.Model):
  title = models.CharField(max_length=255, default='Art and Music Page')
  art_heading = models.CharField(max_length=255, default='Photography')
  music_heading = models.CharField(max_length=255, default='Music')
  style_sheet = models.OneToOneField(
    StyleSheet,
    on_delete=models.CASCADE,
    null=True,
    )

  def __str__(self):
    return self.title

class SacredJourneyPage(models.Model):
  title = models.CharField(max_length=200, default='Sacred Journey Index')
  upcoming_journeys_heading = models.CharField(max_length=20, default='Upcoming Journeys')
  previous_journeys_heading = models.CharField(max_length=20, default='Previous Journeys')
  style_sheet = models.OneToOneField(
    StyleSheet,
    on_delete=models.CASCADE,
    null=True,
    )

  def __str__(self):
    return self.title

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
  title = models.CharField(max_length=255, default='Ministerial Record')
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
  style_sheet = models.OneToOneField(
    StyleSheet,
    on_delete=models.CASCADE,
    null=True,
    )

  def __str__(self):
    return self.title

  def get_fields(self):
    return [(field.name, getattr(self, field.name)) for field in self._meta.fields]
  
  @property
  def pdf_link(self):
    return MEDIA_PREFIX + self.record_pdf.__str__()

class GuidedMeditationPage(models.Model):
  title = models.CharField(max_length=200, default='Guided Meditations')
  main_text = models.TextField(verbose_name='blurb', blank=True, null=True)
  main_image = models.FileField(upload_to='media/meditations/', blank=True, null=True)
  style_sheet = models.OneToOneField(
    StyleSheet,
    on_delete=models.CASCADE,
    null=True,
    )
  
  def __str__(self):
    return str(self.title)

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
  image = models.FileField(upload_to='media/gallery-images/', blank=True, null=True)
  updated_on = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now=True)
  style_sheet = models.OneToOneField(
    StyleSheet,
    on_delete=models.CASCADE,
    null=True,
    )
  
  def __str__(self):
    return str(self.id)
  
  def get_absolute_url(self):
    return reverse('gallery_category', kwargs={'url_cat': slugify(self.get_category_display()) })

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
  title = models.CharField(max_length=200, default='Main Page')
  tagline = models.TextField(blank=True, null=True)
  body = models.TextField(blank=True, null=True)
  blog_image = models.FileField(upload_to='media/ministerial-record-images/', blank=True, null=True)
  spiritual_direction_image = models.FileField(upload_to='media/main-menu-images/', blank=True, null=True)
  guided_meditations_image = models.FileField(upload_to='media/main-menu-images/', blank=True, null=True)
  sacred_journeys_image = models.FileField(upload_to='media/main-menu-images/', blank=True, null=True)
  ministry_image = models.FileField(upload_to='media/main-menu-images/', blank=True, null=True)
  art_and_music_image = models.FileField(upload_to='media/main-menu-images/', blank=True, null=True)
  style_sheet = models.OneToOneField(
    StyleSheet,
    on_delete=models.CASCADE,
    null=True,
    )

  def __str__(self):
    return str(self.title)
  
  def get_fields(self):
    return [(field.name, getattr(self, field.name)) for field in MainPage._meta.fields]

class Post(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  status = models.IntegerField(choices=STATUS, default=1)
  image = models.FileField(upload_to='media/', blank=True, null=True)
  style_sheet = models.OneToOneField(
    StyleSheet,
    on_delete=models.CASCADE,
    null=True,
    )

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

  def get_fields(self):
    return [(field.name, getattr(self, field.name)) for field in self._meta.fields]

  @property
  def image_link(self):
    return MEDIA_PREFIX + self.image.__str__()

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
  title = models.CharField(max_length=200, unique=True)
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
  status = models.IntegerField(choices=STATUS, default=1)
  slug = models.SlugField(max_length=200, unique=True)
  style_sheet = models.OneToOneField(
    StyleSheet,
    on_delete=models.CASCADE,
    null=True,
    )

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('sacred_journey_detail', kwargs={'slug': self.slug})

  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.title)
    super(SacredJourney, self).save(*args, **kwargs)

  @property
  def image_link(self):
    return MEDIA_PREFIX + self.image.__str__()

class SpiritualDirection(models.Model):
  title = models.TextField(blank=True, null=True, default='Spiritual Direction')
  blurb = models.TextField(blank=True, null=True)
  what_is_spiritual_direction_image = models.FileField(upload_to='media/spiritual-direction-images/', blank=True, null=True)
  what_do_spiritual_directors_do_image = models.FileField(upload_to='media/spiritual-direction-images/', blank=True, null=True)
  one_on_one_sessions_image = models.FileField(upload_to='media/spiritual-direction-images/', blank=True, null=True)
  contact_wayne_for_a_session_image = models.FileField(upload_to='media/spiritual-direction-images/', blank=True, null=True)
  what_is_spiritual_direction = models.TextField(blank=True, null=True)
  what_do_spiritual_directors_do = models.TextField(blank=True, null=True)
  one_on_one_sessions = models.TextField(blank=True, null=True)
  contact_wayne_for_a_session = models.TextField(blank=True, null=True)
  style_sheet = models.OneToOneField(
    StyleSheet,
    on_delete=models.CASCADE,
    null=True,
    )

  def __str__(self):
    return self.title

  def get_fields(self):
    return [(field.name, getattr(self, field.name)) for field in self._meta.fields]

class ContactPage(models.Model):
  title = models.CharField(max_length=200, default='Contact')
  blurb = models.TextField(blank=True, null=True)
  image = models.FileField(upload_to='media/contact/', blank=True, null=True)
  phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
  email = models.CharField(max_length=200, blank=True, null=True)
  style_sheet = models.OneToOneField(
    StyleSheet,
    on_delete=models.CASCADE,
    null=True,
    )

  def __str__(self):
    return self.title

  def get_fields(self):
    return [(field.name, getattr(self, field.name)) for field in self._meta.fields]
  
  @property
  def image_link(self):
    return MEDIA_PREFIX + self.image.__str__()