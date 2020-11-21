from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class User(AbstractUser):
    subscribed_on = models.ManyToManyField('self', related_name='subscribers', blank=True)


class Post (models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField ('Текст поста' , max_length=300)
    date_creation = models.DateTimeField('Дата публикации', auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='posts')


# Create your models here.
