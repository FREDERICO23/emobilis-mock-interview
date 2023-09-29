from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserProfileForm, PostForm
from .models import UserProfile, Post


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user-profile') 
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
def user_logout(request):
    logout(request)
    return redirect('login')

# def homepage(request):
#     data = Users.objects.all()
#     return render(request, "home.html")

def profile(request):
    user = request.user
    profile = user.userprofile

    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)

def edit_profile(request):
    user = request.user
    profile = user.userprofile
    form_class = UserProfileForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=profile)        
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    else:
        form = form_class(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile_edit.html', context)

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'post_confirm_delete.html', {'post': post})
