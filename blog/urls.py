from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView,PostDeleteView,PostUpdateView,register,profile,PostListAPI,PostDetailAPI

urlpatterns = [
    path('',PostListView.as_view(), name='post_list'),
    path('register/',register,name = 'register'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    path('post/new/',PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/',PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post_delete'),
    path('profile/',views.profile,name='profile'),
    path('contact/',views.contact_view,name='contact'),
    path('api/post/',PostListAPI.as_view(),name = 'api_post_list'),
    path('api/post/<int:pk>/', PostDetailAPI.as_view(),name = 'api_post_detail'),

    

    
]





