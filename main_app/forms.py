from colorfield.widgets import ColorWidget
from django.forms import ModelForm, TextInput
from .models import (Post, SacredJourney, SlideImage, GalleryImage,
  StyleControl, MainPage, BlogIndexPage, GlobalPostStyle, StyleSheet,
  SpiritualDirection, MinisterialRecord, ArtAndMusicPage, GuidedMeditation,
  GuidedMeditationPage, ContactPage, SacredJourneyPage)
from .widgets import DatePickerInput

######## Defaults ########

widget_settings = {
  'primary_heading_color': ColorWidget,
  'background_color': ColorWidget,
  'heading_color': ColorWidget,
  'header_maintext_color': ColorWidget,
  'header_smalltext_color': ColorWidget,
  'body_color': ColorWidget,
  'byline_color': ColorWidget,
  'tagline_color': ColorWidget,
  'image_heading_color': ColorWidget,
  'footer_color': ColorWidget,
}

exclusions = ('title', 'style_sheet')
mr_exclusions = ('title', 'style_sheet', 'first_name', 'middle_initial',
  'last_name', 'mailing_address', 'city', 'state_prov', 'postal_zip', 'email',
  'website', 'phone_home', 'phone_office', 'phone_mobile', 'present_position',
  'present_position_startdate', 'preliminary_uu_fellowship_startdate',
  'why_are_you_seeking_a_ministry_now',
  'describe_the_new_ministry_you_hope_for', 'awards_and_honors',
  'published_writings', 'personal_and_family_situation',
  'background_and_development', 'denominational_and_community_activities',
  'nonprofessional_interests', 'ministerial_development',
  'ministerial_roles_and_functions',
  'ministerial_skills_and_current_special_interests',
  'approach_to_religious_education', 'role_of_music_and_arts',
  'involvement_in_stewardship', 'theological_orientation',)

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

class ArtAndMusicPageForm(ModelForm):
  class Meta:
    model = ArtAndMusicPage
    exclude = exclusions

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

class BlogIndexPageForm(ModelForm):
  class Meta:
    model = BlogIndexPage
    exclude = exclusions
    widgets = widget_settings

class BlogIndexPageStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    fields = select_fields(model, 'content_heading', 'content_body',
      'byline')
    custom = {
      'content_heading': 'post preview heading',
      'content_body': 'post preview text',
      'byline': 'post info'
    }
    labels = make_labels(fields, **custom)

class ContactPageForm(ModelForm):
  class Meta:
    model = ContactPage
    exclude = exclusions

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

class GlobalPostStyleForm(ModelForm):
  class GlobalPostStyle:
    model = Post
    widgets = {
      'primary_heading_font_color': ColorWidget,
      'body_font_color': ColorWidget,
      'byline_font_color': ColorWidget,
    }

class GuidedMeditationPageForm(ModelForm):
  class Meta:
    model = GuidedMeditationPage
    exclude = exclusions

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

class MainPageForm(ModelForm):
  class Meta:
    model = MainPage
    exclude = exclusions
    widgets = widget_settings
    
class MainPageStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    custom = {'primary_heading': 'tagline and welcome message', }
    fields = select_fields(model, 'primary_heading_', 'image_heading_',
      'body_')
    labels = make_labels(fields, **custom)
    widgets = widget_settings

class MinisterialRecordForm(ModelForm):
  class Meta:
    model = MinisterialRecord
    exclude = mr_exclusions

class MinisterialRecordStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    fields = select_fields(model, 'primary_heading', 'secondary_heading',
      'image_heading', 'tertiary_heading', 'body', 'content_heading',
      'content_body')
    custom = {
      'primary_heading': 'title',
      'secondary_heading': 'video caption',
      'tertiary_heading': 'Ministerial record link/login prompt',
      'body_': 'blurb ',
      'content_heading': 'subheading',
      'content_body': 'subheading text',
    }
    labels = make_labels(fields, **custom)
    widgets = widget_settings

class SpiritualDirectionForm(ModelForm):
  class Meta:
    model = SpiritualDirection
    exclude = exclusions

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

class SacredJourneyPageForm(ModelForm):
  class Meta:
    model = SacredJourneyPage
    exclude = exclusions
    widgets = widget_settings

class SacredJourneyPageStyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    fields = select_fields(model, 'primary_heading', 'content_heading',
      'content_body', 'byline')
    custom = {
      'primary_heading': 'upcoming/previous',
      'content_heading': 'journey preview heading',
      'content_body': 'journey preview text',
      'byline': 'journey info'
    }
    labels = make_labels(fields, **custom)
    widgets = widget_settings

class SlideImageForm(ModelForm):
  class Meta:
    model = SlideImage
    fields = ['image', 'order']

class StyleSheetForm(ModelForm):
  class Meta:
    model = StyleSheet
    exclude = ('parent',)

class StyleControlForm(ModelForm):
  class Meta:
    model = StyleControl
    fields = select_fields(model, 'background_color', 'background_opacity',
      'color', 'opacity', 'heading_color', 'heading_opacity', 'font_family',)
    widgets = widget_settings