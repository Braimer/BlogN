from django.shortcuts import render,get_object_or_404
from .models import Tag,Post,Profile
from django.views import generic       #for class based views

# Create your views here.

#home view ,shows posts
'''def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})'''



'''def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'post_list.html', {'posts': posts})'''


'''def post_list(request):
    posts = Post.objects.filter(published=True)
    #return render(request, 'post_list.html', {'posts': posts})
    if request.user.is_authenticated:
        greeting = f"Hello, {request.user.username}!"  # Greet logged-in user
    else:
        greeting = "Welcome, Guest!"
    
    # Your blog posts logic here
    return render(request, 'post_list.html', {'greeting': greeting})'''


def post_list(request):
    # Get all published posts
    posts = Post.objects.filter(published=True)
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        greeting = f"Hello, {request.user.username}!"  # Greet logged-in user
    else:
        greeting = "Welcome, Guest!"  # Greet guest user
    
    # Pass both the greeting and posts to the template
    return render(request, 'post_list.html', {'posts': posts, 'greeting': greeting})


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


'''def login(request):
    return render(request,'login.html')'''


#  login views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post_list')  # ⬅️ Redirect to your main page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')  # Show the login form'''


