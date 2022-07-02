from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('art-and-music/', views.art_and_music, name='art_and_music'),
  path('art-and-music/<int:pk>/edit-info/', views.ArtAndMusicPageUpdate.as_view(), name='art_and_music_page_update'),
  path('art-and-music/add-music/', views.MusicCreate.as_view(), name='music_create'),
  path('art-and-music/music/<int:pk>/edit/', views.MusicUpdate.as_view(), name='music_update'),
  path('art-and-music/music/<int:pk>/delete/', views.MusicDelete.as_view(), name='music_delete'),
  path('art-and-music/art/<int:pk>/delete-photo/', views.GalleryImageDelete.as_view(), name='delete_photo'),
  path('art-and-music/add-photo/', views.GalleryImageCreate.as_view(), name='add_photo'),
  path('art-and-music/art/<int:pk>/edit-caption/', views.GalleryImageUpdate.as_view(), name='edit_caption'),
  path('art-and-music/<str:url_cat>/', views.photos_category, name='gallery_category'),
  path('guided-meditations/', views.GuidedMeditationList.as_view(), name='guided_meditations'),
  path('guided-meditations/add/', views.GuidedMeditationCreate.as_view(), name='guided_meditation_create'),
  path('guided-meditations/<int:pk>/edit/', views.GuidedMeditationUpdate.as_view(), name='guided_meditation_update'),
  path('guided-meditations/<int:pk>/delete/', views.GuidedMeditationDelete.as_view(), name='guided_meditation_delete'),
  path('guided-meditations/<int:pk>/edit-info/', views.GuidedMeditationPageUpdate.as_view(), name='guided_meditation_page_update'),
  path('ministry/', views.ministry, name="ministry"),
  path('ministry/ministerial-record/', views.ministerial_record, name="ministerial_record"),
  path('ministry/ministerial-record/<int:pk>/edit/', views.MinisterialRecordUpdate.as_view(), name="ministerial_record_update"),
  path('sacred-journeys/', views.sacred_journeys_index, name='sacred_journeys'),
  path('sacred-journeys/add/', views.SacredJourneyCreate.as_view(), name='sacred_journey_create'),
  path('sacred-journeys/<slug:slug>/edit/', views.SacredJourneyUpdate.as_view(), name='sacred_journey_update'),
  path('sacred-journeys/<slug:slug>/delete/', views.SacredJourneyDelete.as_view(), name='sacred_journey_delete'),
  path('sacred-journeys/<slug:slug>/', views.SacredJourneyDetail.as_view(), name='sacred_journey_detail'),
  path('spiritual-direction/', views.spiritual_direction, name='spiritual_direction'),
  path('spiritual-direction/<int:pk>/edit/', views.SpiritualDirectionUpdate.as_view(), name='spiritual_direction_update'),
  path('blog/', views.posts_index, name='blog'),
  path('blog/create/', views.PostCreate.as_view(), name='post_create'),
  path('blog/<slug:slug>/edit/', views.PostUpdate.as_view(), name='post_update'),
  path('blog/<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
  path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
  path('slide-image-<int:pk>/', views.SlideImageDelete.as_view(), name='delete_slide_image'),
  path('<int:main_page_id>/edit-slides/', views.edit_slides, name='edit_slides'),
  path('<int:main_page_id>/edit-slides/add-slide/', views.add_slide_image, name='add_slide_image'),
  path('<int:pk>/edit/', views.MainPageUpdate.as_view(), name='main_page_update'),
  path('<int:pk>/change-styles/', views.StyleControlUpdate.as_view(), name='style_control'),
  path('google2968686464ca0744.html/', views.google_site_verification, name='google'),
]