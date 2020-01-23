
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [


    path('', views.home,name='home'),
    path('profile/', views.profile , name = 'profile'),
    path('update_profile/',views.update_profile,name='update'),
    path('jobs', views.jobs, name='jobs'),
    path('new/job', views.new_job, name='newJob'),
    




]

if settings.DEBUG:
  urlpatterns+= static( settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)