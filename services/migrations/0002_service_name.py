# Generated by Django 4.2.3 on 2023-07-17 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(default='Name', max_length=255),
            preserve_default=False,
        ),
    ]