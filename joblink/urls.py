from django.contrib import admin
from django.urls import path,include
from django .contrib.auth import views
from app.views import *





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('social_django.urls',namespace = 'social')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('',include('app.urls')),

    path('logout/', views.LogoutView.as_view()),
]
