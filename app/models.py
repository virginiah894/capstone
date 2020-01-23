from django.db import models
from django.contrib.auth.models import *


from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import  post_save





class Category(models.Model):
     category = models.CharField(max_length = 60)
     def __str__(self):
        return self.category

class User(AbstractUser):
    is_employer = models.BooleanField('employer status', default=False)
    is_jobseeker  = models.BooleanField('jobseeker status', default=False)
    



class Job(models.Model):
    title = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
  
    posted_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='job/')
    company = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    @classmethod
    def search_post(cls, search_term):
       jobs = cls.objects.filter(Q (user__username=search_term) | Q (company__company=search_term) | Q (title__icontains=search_term))
       return jobs


class Skills(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skillquiz')
    name = models.CharField(max_length=255)
  
class Subject(models.Model):
    name = models.CharField(max_length=30)




class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    skills = models.ManyToManyField(Skills, through='skillquiz')
    interested_jobs = models.ManyToManyField(Job, related_name='interested_jobs')
class skillquiz(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='taken_skills')
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE, related_name='taken_skills')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

  




class Profile(models.Model):
  user= models.OneToOneField(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=70)
  email = models.EmailField(null=True)
  bio = models.CharField(max_length=400)
  picture = models.ImageField(upload_to='profile/',blank=True, default='yummy.jpg')
  category= models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
  qualifications= models.CharField(max_length=1000,null=True)

  def __str__(self):
    return self.name


  @receiver(post_save,sender=User)
  def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    
  @receiver(post_save,sender=User)
  def save_profile(sender, instance,**kwargs):
    instance.profile.save()


