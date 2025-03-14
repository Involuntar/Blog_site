from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    def __str__(self):
        return self.category_name

class Post(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='post/')
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    post_text = models.TextField()
    likes = models.IntegerField(default=0)
    date = models.DateTimeField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.id}. {self.title}'

class Comment(models.Model):
    comment_text = models.TextField()
    likes = models.IntegerField(default=0)
    date = models.DateTimeField()
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL, blank=True)
    def __str__(self):
        return f'{self.id}. {self.comment_text} - {self.post.title}'
