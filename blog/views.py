from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from blog.models import Comment, Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {
        'posts': posts
    })

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    return render(request, 'posts/post.html', {
        'post': post,
        'comments': comments
    })

def comment(request, post_id):
    if request.POST['comment_text'] == '':
        return HttpResponseRedirect(reverse('blog:post', args=(post_id,)))
    comm = Comment.objects.create(
        comment_text=request.POST['comment_text'],
        date=datetime.now(),
        post_id=post_id
    )
    comm.save()
    return HttpResponseRedirect(reverse('blog:post', args=(post_id,)))