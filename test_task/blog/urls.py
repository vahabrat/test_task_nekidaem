from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [

    path('my_blog', views.post_list, name='post_detail'),
    path('users', views.users_list, name='users_list'),
    path('news', views.news, name = 'news'),
]