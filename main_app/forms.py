from django.forms import ModelForm, TextInput
from .models import SacredJourney, SlideImage, GalleryImage, StyleControl
from .widgets import DatePickerInput

class SacredJourneyForm(ModelForm):
  class Meta:
    model = SacredJourney
    exclude = ('slug',)
    widgets = {
      'start_date': DatePickerInput(),
      'end_date': DatePickerInput()
    }

class SlideImageForm(ModelForm):
  class Meta:
    model = SlideImage
    fields = ['image', 'order']

class GalleryImageUpdateForm(ModelForm):
  class Meta:
    model = GalleryImage
    fields = ['caption', 'font_size']

class StyleControlForm(ModelForm):
  class Meta:
    model = StyleControl
    fields = '__all__'
    # widgets = {
    #   'font_color': TextInput(attrs={'type': 'color'}),
    # }