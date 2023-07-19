from django.shortcuts import render, redirect

from reviews.forms import ReviewForm
from reviews.models import Review


def all_reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reviews:all_reviews')
    else:
        form = ReviewForm()
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/all_reviews.html', {
        'reviews': reviews,
        'form': form,
    })

