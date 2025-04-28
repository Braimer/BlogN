
from django.urls import path
from .import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.detail, name='detail'),
    path('tag/<str:tag_name>/', views.tag_posts, name='tag_posts'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('login/',views.login_view,name='login'),
]
   
