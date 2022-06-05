from dataclasses import fields
from urllib import request
from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
