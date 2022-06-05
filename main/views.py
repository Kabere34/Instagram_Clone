from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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

def add_comment(request,image_id):
  current_user =request.user
  if request.method=='POST':
    image_item=Post.objects.filter(id=image_id).first()

    form=CommentForm(request.POST, request.FILES)
    if form.is_valid():
      comment=form.save(commit=False)
      comment.user=current_user
      comment.post=image_item
      comment.save()
      return redirect('home')
    else:
      form=CommentForm()
    return render(request,'main/comment.html',{"form":form,"image_id":image_id})


def search_results(request):
  if 'user' in request.GET and request.GET["user"]:
    search_term = request.GET.get("user")
    searched_user = Profile.search_by_name(search_term)
    message = f"{search_term}"
    return render(request, 'search.html',{"message":message,"searched_user": searched_user})
  else:
       message = "You haven't searched for any term"
       return render(request, 'search.html',{"message":message})







