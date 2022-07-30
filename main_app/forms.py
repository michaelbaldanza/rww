from colorfield.widgets import ColorWidget
from django.forms import ModelForm, TextInput
from .models import (Post, SacredJourney, SlideImage, GalleryImage,
  StyleControl, MainPage, BlogIndexPage, GlobalPostStyle, StyleSheet,
  SpiritualDirection, MinisterialRecord, ArtAndMusicPage, GuidedMeditation,
  GuidedMeditationPage, ContactPage)
from .widgets import DatePickerInput

widget_settings = {
  'primary_heading_color': ColorWidget,
  'background_color': ColorWidget,
  'header_maintext_color': ColorWidget,
  'header_smalltext_color': ColorWidget,
  'body_color': ColorWidget,
  'byline_color': ColorWidget,
  'tagline_color': ColorWidget,
  'image_heading_color': ColorWidget,
}

######## Helper functions ########

def select_fields(some_model, *selected_fields):
  # selects fields to appear in the form
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

######## Forms ########

class ContactPageForm(ModelForm):
  class Meta:
    model = ContactPage
    exclude = ('style_sheet',)

class ContactPageStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    fields = select_fields(model, 'primary_heading', 'body',
      'secondary_heading')
    custom = {
      'primary_heading': 'title',
      'body': 'blurb',
      'secondary_heading': 'contact_info'
    }
    labels = make_labels(fields, **custom)

class GuidedMeditationPageForm(ModelForm):
  class Meta:
    model = GuidedMeditationPage
    exclude = ('style_sheet',)

class GuidedMeditationPageStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    fields = select_fields(model, 'primary_heading', 'body',
      'content_heading', 'content_body',)
    custom = {
      'primary_heading': 'title',
      'body': 'blurb',
      'content_heading': 'meditation heading',
      'content_body': 'description',
    }
    labels = make_labels(fields, **custom)
    widgets = widget_settings

class ArtAndMusicPageForm(ModelForm):
  class Meta:
    model = ArtAndMusicPage
    exclude = ('title', 'style_sheet')

class ArtAndMusicPageStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    fields = select_fields(model, 'primary_heading', 'secondary_heading',
      'image_heading')
    custom = {
      'primary_heading': 'photogtaphy heading',
      'secondary_heading': 'music heading',
    }
    labels = make_labels(fields, **custom)
    widgets = widget_settings

class MinisterialRecordForm(ModelForm):
  class Meta:
    model = MinisterialRecord
    exclude = ('style_sheet',)

class MinisterialRecordStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    fields = select_fields(model, 'primary_heading', 'secondary_heading',
      'image_heading', 'tertiary_heading', 'body')
    custom = {
      'primary_heading': 'title',
      'tertiary_heading': 'subheading',
      'body': 'subheading text'
    }
    labels = make_labels(fields, **custom)
    widgets = widget_settings

class SpiritualDirectionStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    fields = select_fields(model, 'primary_heading',
      'secondary_heading', 'image_heading', 'secondary_heading',
      'tertiary_heading', 'body')
    custom = {
      'primary_heading': 'title',
      'secondary_heading': 'blurb',
      'tertiary_heading': 'question heading',
      'body': 'answer',
    }
    labels = make_labels(fields, **custom)
    widgets = widget_settings

class SpiritualDirectionForm(ModelForm):
  class Meta:
    model = SpiritualDirection
    exclude = ('style_sheet',)

class GlobalPostStyleForm(ModelForm):
  class GlobalPostStyle:
    model = Post
    widgets = {
      'primary_heading_font_color': ColorWidget,
      'body_font_color': ColorWidget,
      'byline_font_color': ColorWidget,
    }

class PostForm(ModelForm):
  class Meta:
    model = Post
    exclude = ('slug', 'style_sheet', 'status')

class PostStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    fields = select_fields(model, 'primary_heading_', 'body_', 'byline_')
    custom = {'primary_heading': 'title'}
    labels = make_labels(fields, **custom)
    widgets = widget_settings

class SacredJourneyForm(ModelForm):
  class Meta:
    model = SacredJourney
    exclude = ('slug', 'status', 'style_sheet',)
    widgets = {
      'start_date': DatePickerInput(),
      'end_date': DatePickerInput()
    }

class SacredJourneyStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    fields = select_fields(model, 'primary_heading', 'body', 'byline')
    custom = {'primary_heading': 'title'}
    labels = make_labels(fields, **custom)
    widgets = widget_settings

class SlideImageForm(ModelForm):
  class Meta:
    model = SlideImage
    fields = ['image', 'order']

class GalleryImageCreateForm(ModelForm):
  class Meta:
    model = GalleryImage
    exclude = ('style_sheet',)

class GalleryImageUpdateForm(ModelForm):
  class Meta:
    model = GalleryImage
    fields = ['caption',]

class GalleryImageStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    fields = select_fields(model, 'body')
    custom = {'body': 'caption'}
    labels = make_labels(fields, **custom)


class StyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    exclude = ('parent',)

class MainPageStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    custom = {'primary_heading': 'tagline'}
    fields = select_fields(model, 'primary_heading_', 'image_heading_',
      'body_')
    labels = make_labels(fields, **custom)
    widgets = widget_settings

class MainPageForm(ModelForm):
  class Meta:
    model = MainPage
    exclude = ('style_sheet',)
    widgets = widget_settings

class BlogIndexPageForm(ModelForm):
  class Meta:
    model = BlogIndexPage
    fields = '__all__'
    widgets = {
      'content_heading_font_color': ColorWidget,
      'content_body_font_color': ColorWidget,
      'byline_font_color': ColorWidget,
    }

class StyleControlForm(ModelForm):
  class Meta:
    model = StyleControl
    fields = '__all__'
    # widgets = {
    #   'font_color': ColorWidget,
    #   'background_color': ColorWidget,
    #   'header_maintext_color': ColorWidget,
    #   'header_smalltext_color': ColorWidget,
    # }
    widgets = widget_settings