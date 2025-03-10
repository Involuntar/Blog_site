from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    post_text = models.TextField()
    likes = models.IntegerField(default=0)
    date = models.DateTimeField()

class Comment(models.Model):
    comment_text = models.TextField()
    likes = models.IntegerField(default=0)
    date = models.DateTimeField()
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
