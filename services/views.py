from django.shortcuts import render

from services.models import Service


def all_services(request):
    services = Service.objects.all()

    return render(request, 'services/all_services.html', {
        'services': services,
    })
