from django.shortcuts import render
from .models import Tag,Post
from django.views import generic       #for class based views

# Create your views here.

#home view ,shows posts
def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})

