from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from PIL import Image


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null = True)
    title = models.TextField(max_length=200)
    content = models.TextField()
    image = models.ImageField()


class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogmodel", null = True)
    category = models.CharField(max_length=100, null = True)
    title = models.CharField(max_length=1000)
    content = FroalaField()
    description = models.CharField(max_length=400, default="")
    slug = models.SlugField(max_length=1000)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    background = models.ImageField(default='defaultbg.jpg', upload_to='postbg')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile") 
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    background = models.ImageField(default='defaultbg.jpg', upload_to='background_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
class Likes(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    blogmodel = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='blog_like')
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(BlogModel, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',)
    content = FroalaField()
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)



