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

