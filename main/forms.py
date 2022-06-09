from dataclasses import fields
from urllib import request
from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm((UserCreationForm)):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=('image','caption')
    exclude=['user']

class ProfileForm(forms.ModelForm):
  class Meta:
    model=Profile
    fields=('name','location','profile_picture', 'bio')
    exclude=['user']

class CommentForm (forms.ModelForm):
  class Meta:
    model=Comment
    exclude=['post','user','profile']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
