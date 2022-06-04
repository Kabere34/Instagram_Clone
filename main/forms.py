from django import forms
from .models import Post
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=('image','caption')

class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=250, help_text='Required. Inform a valid email address.')
  class Meta:
    model=User
    fields=('username', 'email', 'password1', 'password2')
