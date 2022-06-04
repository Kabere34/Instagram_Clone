from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.
def home(request):
  images=Post.objects.all()
  return render(request, 'main/index.html',{'images':images})
def upload(request):
  upload=Post()
  if request.method == 'POST':
    upload=PostForm(request.POST,request.FILES)
    if upload.is_valid():
      upload.save()
      return redirect('home')
    else:
      return HttpResponse('Your form is invalid')
  else:
    return render(request,'upload_form.html',{'upload':upload})

def update_post(request,post_id):
  post_id = int(post_id)
  try:
    post_up=Post.objects.get(id=post_id)
  except Post.DoesNotExist:
    return redirect('home')
  post_form=Post(request.POST or None, instance=post_up)
  if post_form.is_valid():
    post_form.save()
    return redirect('home')
  return render(request,'upload_form.html',{'upload':post_form})




