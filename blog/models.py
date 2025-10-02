from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
# defining post model
class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    publised = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

  



    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic=models.ImageField(upload_to ='profile_pics',blank=True,null=True)
    location=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
    

@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        profile, _ = Profile.objects.get_or_create(user=instance)
        profile.save()



