from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BlogPost
from .models import Like
from .models import Comment
from .models import Notification


@receiver(post_save, sender=BlogPost)
def send_notification_on_blog_create(sender, instance, created, **kwargs):
    if created: 
        Notification.objects.create(recipient=instance.author,
                                    message=f"Your blog '{instance.title}' has been posted successfully!")
        

@receiver(post_save, sender=Like)
def send_notification_on_like(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(recipient=instance.blog.author,
                                message=f" '{instance.user.username}' liked your blog titled: '{instance.blog.title}' ")
        

@receiver(post_save, sender=Comment)
def send_notification_on_comment(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(recipient=instance.blog.author,
                                    message=f" '{instance.user.username}' commented on your blog titled: '{instance.blog.title}' ")