from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):

    if request.method == 'POST':
        Post.objects.create(title=request.POST['title'],text=request.POST['post_text'],user=request.user)
    else:
        pass
    posts = Post.objects.filter(user = request.user)

    return render(request, 'blog/post_list.html',{'posts': posts})


def users_list(request):

    if request.method  == 'POST':
        action = request.POST['action']
        if action == 'subscribe':
            request.user.subscribed_on.add(int(request.POST['subscribe_to']))
        elif action == 'unsubscribe':
            request.user.subscribed_on.remove(int(request.POST['unsubscribe_from']))
            removal_post_read = Post.objects.filter(user_id=int(request.POST['unsubscribe_from']))
            request.user.is_read_list.remove(*removal_post_read)

    print(list(request.user.subscribed_on.all()))

    #users = get_user_model().objects.all()
    users = get_user_model().objects.exclude(id=request.user.id)
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

    if request.method == 'POST':
        action = request.POST['action']
        if action == 'as_un_read':

            request.user.is_read_list.remove(int(request.POST['as_un_read']))
        if action == 'as_read':

            request.user.is_read_list.add(int(request.POST['as_read']))


    users = request.user.subscribed_on.all()
    posts = Post.objects.filter(user__in=users).order_by('-date_creation')

    return render(request, 'blog/news.html',{'posts': posts})
    """return JsonResponse({'posts': [{
        "id": post.id,
        "title": post.title,
    } for post in posts]})"""
# Create your views here.
