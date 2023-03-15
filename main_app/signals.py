from .models import GalleryImage, Post, SacredJourney, Event, StyleSheet
from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver
import random

@receiver(post_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
  print('hitting signals.py delete_post_image')
  instance.image.delete(False)

@receiver(post_save, sender=GalleryImage)
def create_gallery_image_style_sheet(sender, instance, created, **kwargs):
  if created:
    style_sheet = StyleSheet.objects.create(parent=instance.category)
    instance.style_sheet = style_sheet
    instance.save()

@receiver(post_save, sender=Post)
def create_post_style_sheet(sender, instance, created, **kwargs):
  if created:
    style_sheet = StyleSheet.objects.create(parent=instance.slug)
    instance.style_sheet = style_sheet
    instance.save()

@receiver(post_save, sender=SacredJourney)
def create_sacred_journey_style_sheet(sender, instance, created, **kwargs):
  if created:
    style_sheet = StyleSheet.objects.create(parent=instance.slug)
    instance.style_sheet = style_sheet
    instance.save()

@receiver(post_save, sender=Event)
def create_event_style_sheet(sender, instance, created, **kwargs):
  if created:
    style_sheet = StyleSheet.objects.create(parent=instance.slug)
    instance.style_sheet = style_sheet
    instance.save()