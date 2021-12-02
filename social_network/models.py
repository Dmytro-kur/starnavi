from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass


class Post(models.Model):
    """Post model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                            related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['created']


class Like(models.Model):
    """Post's like"""
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                            related_name='user_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                            related_name='post_likes')

    def __str__(self):
        return f"{self.user} likes \'{self.post.title}\'"


class Activity(models.Model):
    """User's activity"""
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='activities')
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        datetime = self.created.strftime("%Y-%m-%d %H:%M:%S")
        request = "'" + self.description.upper() + "'"
        return f"{datetime}: {request} request from \
            {self.user}"

    class Meta:
        verbose_name_plural = "Activities"

