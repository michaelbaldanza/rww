from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from main_app.models import MainPage, MinisterialRecord, Music, Post, SacredJourney

class PostSitemap(Sitemap):
  changefreq = 'weekly'
  priority = 0.9

  def items(self):
    return Post.objects.all()

  def lastmod(self, obj):
    return obj.updated_on

class SacredJourneySitemap(Sitemap):
  changefreq = 'monthly'
  priority = 0.9

  def items(self):
    return SacredJourney.objects.all()

  def lastmod(self, obj):
    return obj.updated_on

class StaticViewsSitemap(Sitemap):
  changefreq = 'monthly'

  def items(self):
    return [
      'art_and_music',
      'guided_meditations',
      'ministerial_record',
      'spiritual_direction',
    ]

  def location(self, item):
    return reverse(item)