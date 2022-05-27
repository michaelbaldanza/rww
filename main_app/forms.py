from django.forms import ModelForm
from .models import SacredJourney, SlideImage, GalleryImage
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
    fields = ['caption']