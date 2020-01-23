from .models import *
from django.contrib.auth.forms import UserCreationForm
from django  import forms
from crispy_forms.helper import FormHelper
from  crispy_forms.layout import Submit,Layout,Field






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
