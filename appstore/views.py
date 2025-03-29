from django.shortcuts import render
from .models import Project,Tag

# Create your views here.
def home(request):
    projects=Project.objects.all()
    tags=Tag.objects.all()
    return render(request,'home.html',{'projects':projects,'tags':tags})

def contacts(request):
    return render(request,"contact.html")


def project(request,id):
    return render(request,"project.html")
