# Generated by Django 3.1.3 on 2020-11-20 18:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscribed_on',
            field=models.ManyToManyField(blank=True, related_name='_user_subscribed_on_+', to=settings.AUTH_USER_MODEL),
        ),
    ]