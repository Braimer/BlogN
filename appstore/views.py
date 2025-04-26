from django.shortcuts import render,get_object_or_404
from .models import Tag,Post,Profile
from django.views import generic       #for class based views

# Create your views here.

#home view ,shows posts
'''def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})'''



def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'post_list.html', {'posts': posts})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'detail.html', {'post': post})

def tag_posts(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag, published=True)
    return render(request, 'tag_posts.html', {'tag': tag, 'posts': posts})

def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    posts = Post.objects.filter(author=profile, published=True)
    return render(request, 'profile.html', {'profile': profile, 'posts': posts})
