from django.shortcuts import render


def all_services(request):
    return render(request, 'services/all_services.html')
