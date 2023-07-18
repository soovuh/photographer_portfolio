from django.shortcuts import render

from reviews.models import Review


def all_reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/all_reviews.html', {
        'reviews': reviews,
    })
