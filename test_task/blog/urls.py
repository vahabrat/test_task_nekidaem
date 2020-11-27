from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('my_blog', views.post_list, name='my_blog'),
    path('users', views.users_list, name='users_list'),
    path('news', views.news, name = 'news'),

    #path('post/<int:post_id>', views.post, name='post'),
    path('post/<int:post_id>', views.NewPost.as_view(), name='post'),

]