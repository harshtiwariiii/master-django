from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.


# listing all the profucts 
class PostListView(ListView):
    model = Post
    template_name =  'blog/post_list.html'
    context_object_name = 'posts'
    ordering =  ['-created_at']
    # posts=Post.objects.filter().order_by('-created_at') #gets all posts from db newest first
    # return render(request,'blog/post_list.html',{'posts':posts}) #render(request, template, context) → renders HTML template with data.


#{'posts':posts} -> passes data to a template as variable



# detailing of post 
class PostDetailView(DetailView):
    model =Post
    template_name='blog/post_detail.html'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author












