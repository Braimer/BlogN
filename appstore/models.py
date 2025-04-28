from django.db import models
from django.conf import settings

# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name
    
#profile models, contain user profile details
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    website=models.URLField(blank=True)
    bio=models.CharField(max_length=240,blank=True)

    def __str__(self):
        return self.user.get_username()
    

#posts model
class Post(models.Model):
    title=models.CharField(max_length=100, unique=True)
    subtitle=models.CharField(max_length=100,blank=True)
    slug=models.SlugField(max_length=100,unique=True)
    content=models.TextField()
    meta_description=models.CharField(max_length=150,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(auto_now=True)
    published=models.BooleanField(default=False)

    author=models.ForeignKey(Profile,on_delete=models.PROTECT)
    tags=models.ManyToManyField(Tag,blank=True)

    class Meta:
        ordering=["-published_date"]

    def __str__(self):
        return self.title


'''abracadabra starts here'''





#user login view
# Example: User login view
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to user profile page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')








#profile model
# Example: User profile model
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Add other profile fields as needed



    #profile view
    # Example: User profile view
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})