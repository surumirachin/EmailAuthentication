
import datetime
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from .models import Post
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email','first_name','last_name','age','gender')
        # field_classes = {"username": forms.UsernameField}



class PostForm(forms.ModelForm):
    

    class Meta:
        model = Post
        fields ="__all__"
