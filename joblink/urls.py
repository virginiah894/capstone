from django.contrib import admin
from django.urls import path,include
from django .contrib.auth import views as auth_views
from app.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('social_django.urls',namespace = 'social')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('',include('app.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
 
    path('accounts/signup/basicuser/', BasicSignUpView.as_view(), name='basicuser'),
    
    path('accounts/signup/jobseeker/', JobSignUpView.as_view(), name='jobseeker'),
    path('accounts/signup/employer/', EmployerSignUpView.as_view(), name='employer'),

    path('logout/', auth_views.LogoutView, {"next_page": '/'}),
]
