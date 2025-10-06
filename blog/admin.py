from django.contrib import admin
from .models import Post, Profile,ContactMessage


# Register your models here.
# admins here 




class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'publised')
    search_fields = ('title', 'body')

admin.site.register(Post, PostAdmin)
admin.site.register(Profile)
admin.site.register(ContactMessage)
