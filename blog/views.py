from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth import login
from .forms import PostForm,UserRegisterForm,ProfileUpdateForm,ContactForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from rest_framework import generics
from .serializers import PostSerializer


# Create your views here.


# listing all the profucts 
class PostListView(ListView):
    model = Post
    template_name =  'blog/post_list.html'
    context_object_name = 'posts'
    ordering =  ['-created_at']
    paginate_by =5
    # posts=Post.objects.filter().order_by('-created_at') #gets all posts from db newest first
    # return render(request,'blog/post_list.html',{'posts':posts}) #render(request, template, context) → renders HTML template with data.


#{'posts':posts} -> passes data to a template as variable



# detailing of post 
class PostDetailView(DetailView):
    model =Post
    template_name='blog/post_detail.html'


# creating a post
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# updating a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  

# deleting a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



# user registration view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # CHECK IF USER SUBMMITEDTHE FORM 
        if form.is_valid():#VALIDATE THE FROM USER/PAS
            user = form.save()#CREATING USER AT DATABASE 
            login(request,user)#LOGIN THE USER IMMEDATLY AFTER REGISTRATION
            return redirect('login')
    else:
         form = UserRegisterForm()

    return render(request,'blog/register.html',{'form':form})



@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile) # request.FILES for profile picture required 
        if form.is_valid():
            form.save()
            # messages.success(request,"your profile has been updated!")
            # return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request,'blog/profile.html',{'form':form})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Normally we’d send an email or save the data here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Just show a success message for now
            messages.success(request, f"Thanks {name}, your message has been received!")
            return redirect('contact')  # redirect to the same page to clear the form
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})
            
           

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form =PostForm()
    return render(request,'blog/psot_form.html',{'form':form})



class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    

            










