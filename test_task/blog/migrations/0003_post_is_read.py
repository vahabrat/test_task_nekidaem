# Generated by Django 3.1.3 on 2020-11-21 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201120_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
