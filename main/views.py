from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
  # form=PostForm
  # # images=Post.objects.all()
  post = Post.objects.all()
  return render(request, 'main/index.html',{'post':post})

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
def profile(request, username=None):
  '''
	Method that fetches a users profile page
	'''
  current_user =request.user
  us_images=Post.objects.filter(user=current_user.profile)
  return render(request,"main/profile.html",{"us_images":us_images})


@login_required(login_url='/accounts/login/')
def profile_edit(request):
  current_user =request.user
  if request.method=='POST':
    form=ProfileForm(request.POST,request.FILES)
    if form.is_valid():
      image=form.save(commit=False)
      image.user=current_user
      image.save()
      return redirect('profile')
  else:
      form=ProfileForm()
  return render(request,'main/profile_edit.html',{"form":form})


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


def search_results(request):
  if 'user' in request.GET and request.GET["user"]:
    search_term = request.GET.get("user")
    searched_user = Profile.search_by_name(search_term)
    message = f"{search_term}"
    return render(request, 'search.html',{"message":message,"searched_user": searched_user})


def  likepost(request,post_id):
  likes=1
  posts=Post.objects.get(id=post_id)
  posts.likes=posts.likes+1
  posts.save()
  return redirect('home')





