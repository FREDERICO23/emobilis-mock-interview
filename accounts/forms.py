from django import forms
from .models import UserProfile, Post

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
