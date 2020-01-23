from .models import *
from django.contrib.auth.forms import UserCreationForm
from django  import forms
from crispy_forms.helper import FormHelper
from  crispy_forms.layout import Submit,Layout,Field

from django.db import transaction
from app.models import *



    
class JobSignUpForm(UserCreationForm):
    interested_jobs = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_jobseeker = True
        user.save()
        jobseeker = User.objects.create(user=user)
        jobseeker.interests.add(*self.cleaned_data.get('interested_jobs'))
        return user


class EmployerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employer = True
        if commit:
            user.save()
        return user


class BasicSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_basic = True
        if commit:
            user.save()
        return user





class AccountUpdate(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']


class DetailsUpdate(forms.ModelForm):
  class Meta:
    model = Profile
    exclude= ['user']  

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['user', 'category','posted_date']


# class UserCreationForm(UserCreationForm):
#     # interests = forms.ModelMultipleChoiceField(
#     #     queryset=Subject.objects.all(),
#     #     widget=forms.CheckboxSelectMultiple,
#     #     required=True
#     # )

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_basic = True
#         user.save()
#         return user
