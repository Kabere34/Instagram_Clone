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
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
  post = Post.objects.all()
  all_users=User.objects.all()
  return render(request, 'main/index.html',{'all_users':all_users,'post':post[::-1]})

def single_post(request):
  # current_user =request.user
  # if request.method=='POST':
  #   image_item=Post.objects.filter(id=post_id).first()
  return render(request, 'main/single_post.html')



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


@login_required(login_url='/accounts/login/')
def profile_edit(request):
  current_user =request.user
  if request.method=='POST':
    form=ProfileForm(request.POST,request.FILES)
    if form.is_valid():
      image=form.save(commit=False)
      image.user=current_user
      # image.save()
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
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'instagram/results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'main/search.html', {'message': message})

# def search_results(request):
#   if 'user' in request.GET and request.GET["user"]:
#     search_term = request.GET.get("user")
#     searched_user = Profile.search_by_name(search_term)
#     message = f"{search_term}"
#     return render(request, 'search.html',{"message":message,"searched_user": searched_user})
#   else:
#     message = "You haven't searched for any term"
#     return render(request, 'main/search.html',{"message":message})


# def likePost(request,post_id):
#   likes=1
#   posts=Post.objects.get(id=post_id)
#   posts.likes=posts.likes+1
#   posts.save()
#   return redirect('home')
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

  # HttpResponseRedirect(url 'home'current_likes)
  # response=HttpResponse(current_likes)
  # response['Content-Type']='application/json'
  # return response






