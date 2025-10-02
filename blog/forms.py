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



class ContactForm(forms.Form):
    name= forms.CharField(max_length=100,required=True,label="Your Name")
    email = forms.EmailField(required=True,label="Your Email")
    message = forms.CharField(widget=forms.Textarea,required=True,label="Your Message")\
    

    # custom validation for name field  
    def clean_name(self):
        data = self.cleaned_data['name']
        if "@" in data:
            raise forms.ValidationError("Name cannot contain @ symbol")
        return data



        




