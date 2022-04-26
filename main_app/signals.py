from .models import Post
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
  print('hitting signals.py delete_post_image')
  instance.image.delete(False)