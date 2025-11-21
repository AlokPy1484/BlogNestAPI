from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser


# Create your models here.

#building a custom user model
# class User(AbstractUser):



class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(auto_now_add=True)
    # likes = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    #if a user is deleted then all related comments will be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        #newest updated item first if same then newest created
        ordering = ['-updated','-created']
        
    def __str__(self):
        return self.body



class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    title = models.CharField(max_length=100)
    topics = models.ManyToManyField(Topic, related_name="category")

    def __str__(self):
        return self.title
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profile/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Symmetrical ManyToManyField for friends
    follower = models.ManyToManyField("self", symmetrical=False, blank=True)
    

    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'blog'], name='unique_like')
        ]
    

class Request(models.Model):
    requester = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="requester")
    responder = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="responder")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default="pending")  

    class Meta:
        unique_together = ("requester", "responder")

class Notification(models.Model):

    recipient = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, related_name="notification")
    message = models.CharField(max_length=255, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.message