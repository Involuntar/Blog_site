from datetime import datetime
import math
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.paginator import Paginator

from blog.models import Comment, Post

# Create your views here.
def index(request):
    if request.GET.get('search'):
        posts = Post.objects.filter(title=request.GET.get('search')) | Post.objects.filter(author=request.GET.get('search')) | \
        Post.objects.filter(post_text=request.GET.get('search'))
    else:
        posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    pages = math.ceil(len(posts) / 5)
    posts_on_page = paginator.get_page(page_number)
    return render(request, 'posts/index.html', {
        'posts': posts_on_page,
        'range': range(pages)
    })

def post_get(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    paginator = Paginator(comments, 10)
    page_number = request.GET.get('page')
    pages = math.ceil(len(comments) / 10)
    comments_on_page = paginator.get_page(page_number)
    return render(request, 'posts/post.html', {
        'post': post,
        'comments': comments_on_page,
        'range': range(pages)
    })

def comment_create(request, post_id):
    if request.POST['comment_text'] == '':
        return HttpResponseRedirect(reverse('blog:post_get', args=(post_id,)))
    comm = Comment.objects.create(
        comment_text=request.POST['comment_text'],
        date=datetime.now(),
        post_id=post_id
    )
    comm.save()
    return HttpResponseRedirect(reverse('blog:post_get', args=(post_id,)))