# Generated by Django 4.2.3 on 2023-07-22 13:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='owner_review',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(30), django.core.validators.MaxLengthValidator(1000)]),
        ),
    ]
