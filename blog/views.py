from django.core.paginator import Paginator
from django.shortcuts import render

from blog.models import Post


def all_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    posts_per_page = 1
    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/all.html', {
        'posts': page_obj,
    })
