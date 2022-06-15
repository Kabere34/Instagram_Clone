from django import template
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import loader
from .email import send_welcome_email
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      name=form.cleaned_data['username']
      email=form.cleaned_data['email']

      recipient=NewsLetterRecipients(name=name,email=email)
      recipient.save()
      send_welcome_email(name,email)
      form.save()
      return HttpResponseRedirect(reverse('home'))
    else:
      form=RegistrationForm()
    return render(request, 'registration/registration_form.html',{'form':form})


@login_required(login_url='/accounts/login/')
def home(request):
  post = Post.objects.all()
  all_users=User.objects.all()
  return render(request, 'main/index.html',{'all_users':all_users,'post':post[::-1]})


def single_post(request,post_id):
  post=get_object_or_404(Post,id=post_id)

  return render(request, 'main/single_post.html', {"post":post})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    # post = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user.profile
            post.save()

        return redirect('home')
    else:
        form = PostForm()
    return render(request, 'main/new_post.html', {"form": form})


# create and edit profile
@login_required(login_url='/accounts/login/')
def profile(request):
  '''
	Method that fetches a users profile page
	'''
  current_user =request.user
  user=User.objects.all()
  profile_image=Profile.objects.filter(user=request.user.pk)
  print(user,profile_image)
  return render(request,"main/profile.html" ,{"profile":profile, "current_user":current_user})

def user_profile(request,user_id):
  user=get_object_or_404(User,id=user_id)
  return render(request,"main/profile.html" ,{"profile":profile, "current_user":user})


@login_required(login_url='/accounts/login/')
def profile_edit(request):
  current_user =request.user
  if request.method=='POST':
    form=ProfileForm(request.POST,request.FILES)
    if form.is_valid():
      image=form.save(commit=False)
      image.user=current_user
      return redirect('profile')
  else:
      form=ProfileForm()
  return render(request,'main/profile_edit.html',{"form":form})

@login_required(login_url='/accounts/login/')
def add_comment(request,post_id):
  current_user =request.user
  if request.method=='POST':
    image_item=Post.objects.filter(id=post_id).first()

    form=CommentForm(request.POST, request.FILES)
    if form.is_valid():
      comment=form.save(commit=False)
      comment.user=current_user.profile
      comment.post=image_item
      comment.save()
      return redirect('home')
  else:
      form=CommentForm()
  return render(request,'main/comment.html',{"form":form,"post_id":post_id})



@login_required(login_url='/accounts/login/')
def search_results(request):
    post = Post.objects.all()
    query=request.GET.get('query')
    if query:
      image=Post.objects.filter( Q(name__icontains=query) )
      profile=Profile.objects.filter( Q(user__username__icontains=query) )

      params = {
          'image': image,
          'profile': profile,
          'post':post


      }
      return render(request, 'main/search.html', params)

@login_required(login_url='/accounts/login/')
def likePost(request,post_id):
  user=request.user
  post=Post.objects.get(id=post_id)
  current_likes=post.likes
  print(type(current_likes),'current_likes')
  liked=Like.objects.filter(user=user,post=post).count()
  if not liked:
    liked=Like.objects.create(user=user,post=post)
    current_likes=current_likes+1

  else:
    liked=Like.objects.filter(user=user,post=post).delete()
    current_likes=current_likes- 1
  post.likes=current_likes
  post.save()
  print(post)
  return HttpResponseRedirect(reverse('home'))










