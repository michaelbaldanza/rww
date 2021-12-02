from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('art-and-music/', views.art_and_music, name='art_and_music'),
  path('art-and-music/<str:category>', views.photos_category, name='photos_category'),
  path('art-and-music/photos/', views.photos, name='photos'),
  path('art-and-music/photos/mystical-moments', views.photos_mystical, name='photos_mystical'),
  path('art-and-music/photos/people', views.photos_people, name='photos_people'),
  path('art-and-music/photos/nature', views.photos_nature, name='photos_nature'),
  path('art-and-music/photos/places', views.photos_places, name='photos_places'),
  path('guided-meditations/', views.meditations_index, name='meditations'),
  path('ministry/', views.ministry, name="ministry"),
  path('music/', views.music, name="music"),
  path('sacred-journeys/', views.sacred_journeys, name='journeys'),
  path('spiritual-direction/', views.spiritual_direction, name='direction'),
  path('blog/', views.PostList.as_view(), name='blog'),
  path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]