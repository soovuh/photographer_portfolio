from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from blog.models import Post


def all_posts(request):
    posts = Post.objects.all().order_by('-created_at')

    posts_per_page = 10
    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    liked_posts_ids = request.COOKIES.get('liked_posts', '').split(',')
    liked_posts_ids = [int(post_id) for post_id in liked_posts_ids if post_id]

    return render(request, 'blog/all.html', {
        'posts': page_obj,
        'liked_posts': liked_posts_ids,
    })


def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)

    liked_posts_ids = request.COOKIES.get('liked_posts', '').split(',')
    liked_posts_ids = [int(post_id) for post_id in liked_posts_ids if post_id]

    if post_id not in liked_posts_ids:
        post.likes += 1
        post.save()
        liked_posts_ids.append(post_id)
        response = JsonResponse({'message': 'success'})
        response.set_cookie('liked_posts', ','.join(str(pid) for pid in liked_posts_ids))
    else:
        response = JsonResponse({'message': 'rejected'})
    return response
