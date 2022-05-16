from django.forms import ModelForm
from .models import SlideImage

class SlideImageForm(ModelForm):
  class Meta:
    model = SlideImage
    fields = ['image', 'order']