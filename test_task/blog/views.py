from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):

    posts = Post.objects.filter(user = request.user)


    return render(request, 'blog/post_list.html',{'posts': posts})


def users_list(request):

    if request.method  == 'POST':
        action = request.POST['action']
        if action == 'subscribe':
            request.user.subscribed_on.add(int(request.POST['subscribe_to']))
        elif action == 'unsubscribe':
            request.user.subscribed_on.remove(int(request.POST['unsubscribe_from']))

    print(list(request.user.subscribed_on.all()))

    users = get_user_model().objects.all()

    return render(request, 'blog/users_list.html',{'users': users})


def my_filter(func, iterable):
    massive = []
    for item in iterable:
        if func(item)==True:
            massive.append(item)
    return massive

def some_func_iter(item):
    return item>3


def some_function():
    a=[1,2,3,4,5,6,7]

    r = my_filter(some_func_iter,a)

    print(r)


def news(request):

    some_function()

    #posts = Post.objects.filter(user__in=request.user)
    users = request.user.subscribed_on.all()
    posts = Post.objects.filter(user__in=users).order_by('-date_creation')









    return render(request, 'blog/news.html',{'posts': posts})
# Create your views here.
