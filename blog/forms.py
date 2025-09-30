from django import forms
from .models import Post


class PostForm(forms.ModelForm): # forms.Modelform create a form from our model
    class Meta:# tells which model is to used and which fields to include
        model = Post
        fields = {'title','body','publised'}

