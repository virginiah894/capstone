from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from django.contrib import messages
from .forms import AccountUpdate, DetailsUpdate,JobForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,ListView,DetailView,CreateView
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from app.forms import *

# app/post_list.html


class PostListView(ListView):
    model = Job
    template_name = 'index.html'
    context_object_name = 'jobs'
    ordering = ['-posted_date']




class PostDetailView(DetailView):
    model = Job
    template_name='job_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title','category','image','details']
    template_name='post_form.html'
    success_url= ('/')

  

def home(request):
    jobs = Job.objects.all()
    return render(request,'index.html',locals())

def profile(request):
  current_user = request.user
  profile = Profile.objects.filter(user = request.user)
  queryset = Job.objects.all()[::-1]
  class Meta:
    ordering = ['posted_date']


  return render(request,'profile.html',locals())


@login_required(login_url='/accounts/login/')
def update_profile(request):
  
  if request.method == 'POST':
       user_form = AccountUpdate(request.POST,instance=request.user)
       details_form = DetailsUpdate(request.POST ,request.FILES,instance=request.user.profile)
       if user_form.is_valid() and details_form.is_valid():
          user_form.save()
          details_form.save()
          messages.success(request,f'Your Profile account has been updated successfully')
          return redirect('/')
  else:
  

      user_form = AccountUpdate(instance=request.user)
      
      details_form = DetailsUpdate(instance=request.user.profile) 
  forms = {
    'user_form':user_form,
    'details_form':details_form
  }
  return render(request,'update_profile.html',forms)
@login_required(login_url='/accounts/login/')
def jobs(request):
    current_user=request.user
    profile = Profile.objects.get(user=current_user)
    jobs = Job.objects.all()

    return render(request, 'jobs.html', {"jobs":jobs})



@login_required(login_url='/accounts/login/')
def new_job(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)

    if request.method == 'POST':
        form  = JobForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = current_user
            post.category = profile.category
            post.save()

        return HttpResponseRedirect('/')

    else:
        form =JobForm()

    return render(request, 'job_form.html', {"form":form})




