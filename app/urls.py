
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [


    path('', PostListView.as_view(),name='home'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('job/<int:pk>/',PostDetailView.as_view(),name='job-detail'),
    path('profile/', views.profile , name = 'profile'),
    path('posts/', views.posts, name = 'posts'),
    path('job/<int:pk>/update/', PostUpdateView.as_view(),name='update-job'),
    path('job/<int:pk>/delete/', PostDeleteView.as_view(),name='delete-job'),
    path('search/',views.search_results, name='search_results'),

    path('update_profile/',views.update_profile,name='update'),
    path('jobs', views.jobs, name='jobs'),
    path('new/job', views.new_job, name='newJob'),
    




]

if settings.DEBUG:
  urlpatterns+= static( settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)