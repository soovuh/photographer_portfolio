from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from home.forms import ContactForm


def index(request):
    return render(request, 'home/index.html')


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            content = form.cleaned_data.get('content')
            html = render_to_string('home/email_template.html', {
                'name': name,
                'email': email,
                'content': content,
            })
            plain_message = strip_tags(html)
            send_mail(
                subject='Email From Site',
                message=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                html_message=html,
            )
            return redirect('home:contacts')
    else:
        form = ContactForm()
    return render(request, 'home/contacts.html', {
        'form': form,
    })
