from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('art-and-music/', views.art_and_music, name='art_and_music'),
  path('art-and-music/<str:url_cat>/', views.photos_category, name='photos_category'),
  path('guided-meditations/', views.meditations_index, name='guided_meditations'),
  path('ministry/', views.ministry, name="ministry"),
  path('ministry/ministerial-record/', views.ministerial_record, name="ministerial_record"),
  path('ministry/ministerial-record/<int:pk>/edit/', views.MinisterialRecordUpdate.as_view(), name="ministerial_record_update"),
  path('music/', views.music, name="music"),
  path('sacred-journeys/', views.sacred_journeys_index, name='sacred_journeys'),
  path('sacred-journeys/<slug:slug>/edit/', views.SacredJourneyUpdate.as_view(), name='sacred_journey_update'),
  path('sacred-journeys/<slug:slug>/delete/', views.SacredJourneyDelete.as_view(), name='sacred_journey_delete'),
  path('sacred-journeys/<slug:slug>/', views.SacredJourneyDetail.as_view(), name='sacred_journey_detail'),
  path('spiritual-direction/', views.spiritual_direction, name='spiritual_direction'),
  path('blog/', views.posts_index, name='blog'),
  path('blog/create/', views.PostCreate.as_view(), name='post_create'),
  path('blog/<slug:slug>/edit/', views.PostUpdate.as_view(), name='post_update'),
  path('blog/<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
  path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]