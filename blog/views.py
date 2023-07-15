from django.shortcuts import render

from blog.models import Post


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/all.html', {
        'posts': posts,
    })
