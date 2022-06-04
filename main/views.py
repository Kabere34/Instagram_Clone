from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# Create your views here.

# def signup(request):
#   # if request.method == 'POST':
#   #   form=SignUpForm(request.POST)
#   #   if form.is_valid():
#   #     form.save()
#   #     username=form.cleaned_data["username"]
#   #     raw_password=form.cleaned_data["password1"]
#   #     user=authenticate(username=username,password=raw_password)
#   #     login(request, user)
#   #     return redirect('index')
#   # else:
#   #   form=SignUpForm()
#     return render(request, 'registration/registration_form.html')



def home(request):
  # form=PostForm
  # # images=Post.objects.all()
  return render(request, 'main/index.html')


def create_post(request):
   form=PostForm
   images=Post.objects.all()
   return render(request, 'main/create_post.html',{'form':form, 'images':images})
def upload(request):
  upload=Post()
  if request.method == 'POST':
    upload=PostForm(request.POST,request.FILES)
    if upload.is_valid():
      upload.save()
      return redirect('create_post')
    else:
      return HttpResponse('Your form is invalid')
  else:
    return render(request,'upload_form.html',{'upload':upload})

def update_post(request,post_id):
  post_id = int(post_id)
  try:
    post_up=Post.objects.get(id=post_id)
  except Post.DoesNotExist:
    return redirect('create_post')
  post_form=Post(request.POST or None, instance=post_up)
  if post_form.is_valid():
    post_form.save()
    return redirect('create_post')
  return render(request,'upload_form.html',{'upload':post_form})


def delete_post(request,post_id):
  post_id = int(post_id)
  try:
    post_up=Post.objects.get(id=post_id)
  except Post.DoesNotExist:
    return redirect('create_post')
  post_up.delete()
  return redirect('create_post')
