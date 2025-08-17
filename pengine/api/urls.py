from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('user/create', views.createUser, name='createUser'),
    path('posts', views.posts, name='posts'),
    path('post/create', views.createPost, name='createPost'),
]