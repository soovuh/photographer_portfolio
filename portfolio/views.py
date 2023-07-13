from django.shortcuts import render

from portfolio.models import Category


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
