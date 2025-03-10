from django.contrib import admin

from . import models

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment_text', 'likes', 'date']
admin.site.register(models.Comment, CommentAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'post_text', 'likes', 'date']
admin.site.register(models.Post, PostAdmin)