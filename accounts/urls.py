from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list,name='home'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('edit/', edit_profile, name='profile-edit'),
    path('profile/', profile, name='user-profile'),    
    path('post/new/', post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_update, name='post_update'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
]

