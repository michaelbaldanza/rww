from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('art-and-music/', views.art_and_music, name='art_and_music'),
  path('guided-meditations/', views.meditations_index, name='meditations'),
  path('ministry/', views.ministry, name="ministry"),
  path('music/', views.music, name="music"),
  path('photography/', views.photography, name="photography"),
  path('sacred-journeys/', views.sacred_journeys, name='journeys'),
  path('spiritual-direction/', views.spiritual_direction, name='direction'),
  path('blog/', views.PostList.as_view(), name='blog'),
  path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]