from django.shortcuts import render, get_object_or_404

from portfolio.models import Category, Photo


def all_categories(request):
    categories = Category.objects.all()
    category_columns = {'1': [], '2': [], '3': []}
    num = '1'
    for category in categories:
        category_columns[num].append(category)
        if num == '3':
            num = '1'
            continue
        num = str(int(num) + 1)
    return render(request, 'portfolio/portfolio.html', {
        'column_1': category_columns['1'],
        'column_2': category_columns['2'],
        'column_3': category_columns['3']
    })


def category_photos(request, pk):
    category = get_object_or_404(Category, pk=pk)
    related_photos = Photo.objects.filter(category=category).order_by('-id')
    photo_columns = {'1': [], '2': []}
    num = '1'
    for photo in related_photos:
        photo_columns[num].append(photo)
        if num == '1':
            num = '2'
            continue
        num = '1'
    return render(request, 'portfolio/category.html', {
        'column_1': photo_columns['1'],
        'column_2': photo_columns['2'],
        'category_name': category.name,
    })


