from django import forms
from .models import Post,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm): # forms.Modelform create a form from our model
    class Meta:# tells which model is to used and which fields to include
        model = Post
        fields = {'title','body','publised'}

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic','location']

        




