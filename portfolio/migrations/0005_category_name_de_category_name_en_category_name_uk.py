# Generated by Django 4.2.3 on 2023-07-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_category_main_image_alter_photo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uk',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
