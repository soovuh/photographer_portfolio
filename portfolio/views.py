from django.shortcuts import render


def all_categories(request):
    return render(request, 'portfolio/portfolio.html')
