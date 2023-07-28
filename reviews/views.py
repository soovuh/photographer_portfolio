from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from reviews.forms import ReviewForm
from reviews.models import Review


def all_reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('owner_name')
            social = form.cleaned_data.get('owner_social')
            text = form.cleaned_data.get('owner_review')
            html = render_to_string('reviews/new_review_email.html', {
                'name': name,
                'social': social,
                'text': text,
            })
            plain_message = strip_tags(html)
            send_mail(
                subject='New Review From Site',
                message=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                html_message=html,
            )
            return redirect('reviews:all_reviews')
    else:
        form = ReviewForm()
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/all_reviews.html', {
        'reviews': reviews,
        'form': form,
    })

