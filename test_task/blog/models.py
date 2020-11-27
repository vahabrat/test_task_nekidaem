from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models

from django.urls import reverse


class User(AbstractUser):
    subscribed_on = models.ManyToManyField('self', related_name='subscribers', blank=True)
    is_read_list = models.ManyToManyField('Post', related_name='is_read_post', blank=True)

class Post (models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField ('Текст поста' , max_length=300)
    date_creation = models.DateTimeField('Дата публикации', auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='posts')

    def save(self, **kwargs):

        is_new = self.id is None

        super().save(**kwargs)

        if is_new:
            # Отправка адреса с новым постом
            url_message = 'http://127.0.0.1:8000' + reverse('blog:post', args=[self.id])
            subject = self.title
            #users = get_user_model().objects.exclude(id=self.user.id)
            #emails = [user.email for user in users]
            emails = get_user_model().objects.exclude(id=self.user.id).values_list('email', flat=True)

            send_mail(subject, url_message, 'inokentiybest12@gmail.com', emails, fail_silently=False)