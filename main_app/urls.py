from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('art-and-music/', views.art, name='art'),
  path('essays/', views.essays, name='essays'),
  path('guided-meditations/', views.meditations, name='meditations'),
  path('sacred-journeys/', views.sacred, name='sacred'),
  path('blog/', views.PostList.as_view(), name='blog'),
  path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]