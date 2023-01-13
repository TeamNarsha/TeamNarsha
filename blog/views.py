from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    return render(request, 
        'blog/index.html',
        {
            'posts' : posts
        })

def process(request):
    p_post = Post.objects.all()
    return render(request,
        'blog/process.html', 
        { 'p_post' : p_post}
    )

def narsha_single_pages(request,value):
    post=Post.objects.get(pk=value)

    return render(
        request,
        'blog/narsha_single_pages.html',
        {
            'post' : post
        }
    )