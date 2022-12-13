from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO

image_types = {
  'jpg': 'JPEG',
  'jpeg': 'JPEG',
  'png': 'PNG',
  'gif': 'GIF',
  'tif': 'TIFF',
  'tiff': 'TIFF',
}

def image_resize(image):
  img = Image.open(image)
  print('The width of the image is ', img.width)
  print('The height of the image is ', img.height)
  max_size = (1500, 1500)
  if img.width > 1500 or img.height > 1500:
    icc_profile = img.info.get('icc_profile')
    img.thumbnail(max_size)
    img_filename = Path(image.file.name).name
    img_suffix = Path(image.file.name).name.split('.')[-1]
    img_format = image_types[img_suffix]
    buffer = BytesIO()
    img.save(buffer, format=img_format, icc_profile=icc_profile)
    file_object = File(buffer)
    image.save(img_filename, file_object)