from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('art-and-music/', views.art_and_music, name='art_and_music'),
  path('art-and-music/<str:url_cat>/', views.photos_category, name='photos_category'),
  path('guided-meditations/', views.meditations_index, name='guided_meditations'),
  path('ministry/', views.ministry, name="ministry"),
  path('music/', views.music, name="music"),
  path('sacred-journeys/', views.sacred_journeys, name='sacred_journeys'),
  path('spiritual-direction/', views.spiritual_direction, name='spiritual_direction'),
  path('blog/', views.posts_index, name='blog'),
  path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]