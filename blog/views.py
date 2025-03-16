from datetime import datetime
import math
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.paginator import Paginator
from django.views import View

from blog.models import Category, Comment, Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    if request.GET.get('search'):
        posts = posts.filter(title__contains=request.GET.get('search')) | posts.filter(author__contains=request.GET.get('search')) | \
        posts.filter(post_text__contains=request.GET.get('search'))

    if request.GET.getlist('category'):
        posts = posts.filter(category_id__in=request.GET.getlist('category'))

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    pages = math.ceil(len(posts) / 5)
    posts_on_page = paginator.get_page(page_number)
    categories = Category.objects.all()

    args = {
        'posts': posts_on_page,
        'range': range(pages),
        'categories': categories,
    }

    if request.GET.getlist('category'):
        args['selected_categories'] = [ int(cat) for cat in request.GET.getlist('category') ]

    return render(request, 'posts/index.html', args)

def post_get(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    paginator = Paginator(comments, 4)
    page_number = request.GET.get('page')
    pages = math.ceil(len(comments) / 4)
    comments_on_page = paginator.get_page(page_number)
    return render(request, 'posts/post.html', {
        'post': post,
        'comments': comments_on_page,
        'range': range(pages),
        'amount_comments': len(comments)
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