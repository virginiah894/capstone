from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from django.contrib import messages
from .forms import AccountUpdate, DetailsUpdate,JobForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from app.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# app/post_list.html


class PostListView(LoginRequiredMixin,ListView):
    model = Job
    template_name = 'index.html'
    context_object_name = 'jobs'
    ordering = ['-posted_date']




class PostDetailView(LoginRequiredMixin,DetailView):
    model = Job
    template_name='job_detail.html'


class PostCreateView(LoginRequiredMixin,CreateView):
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


@login_required(login_url='/accounts/login')
def posts(request):
  current_user= request.user
  profile=Profile.objects.get(user=current_user)
  posts=Post.objects.all()
  return render(request,'posts.html',{'posts':posts})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ['title', 'description','link']
    template_name= 'job_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.user:
            return True
        return False




def search_results(request):

    if 'job' in request.GET and request.GET["job"]:
        search_term = request.GET.get("job")
        searched_jobs= Job.search_job(search_term)
        message = f"{search_term}"
        print(jsearched_jobs.title)

        return render(request, 'search.html',{"message":message,"jobs": searched_jobs})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    template_name= 'job_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.user:
            return True
        return False







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




