from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView

from .forms import CreatePostForm
from .models import Post


class NewPost(ListView):

    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_queryset(self):
        post_id = self.kwargs.get('post_id', None)  # Получаем аргумент из ссылки
        return Post.objects.filter(id=post_id)


# def post(request, post_id):
#    post=Post.objects.filter(id=post_id)
#    context={'post':post}
#    print(post)
#    return render(request, 'blog/post.html', context)


class PostList(ListView):
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        return context


def post_list(request):
    posts = Post.objects.filter(user=request.user).order_by('date_creation')

    context = {
        'posts': posts,
        'form':CreatePostForm()
    }

    if request.method == 'POST':
        form = CreatePostForm(request.POST)

        if form.is_valid():
            form.save(request.user)
            form = CreatePostForm()
            context['form'] = form


        '''no_errors = True

        if len(request.POST['title']) > 50:
            more_than_err = "Количество символов превышает допустимое значение!!!!!!"
            context['error_title'] = more_than_err
            no_errors = False

        if len(request.POST['title']) == 0:
            error_title = 'Это поле не может быть пустым'
            context['error_title'] = error_title
            no_errors = False



        if len(request.POST['post_text']) > 300:  # bool('')False           #bool('adsadasd')True
            more_error = 'Количество символов превышает допустимое значение!!!!!!'
            context['error_post_text'] = more_error
            no_errors = False

        if len(request.POST['post_text']) == 0:  # bool('')False           #bool('adsadasd')True
            error_post_text = 'Это поле не может быть пустым'
            context['error_post_text'] = error_post_text
            no_errors = False

        if no_errors:
            current_post = Post.objects.create(title=request.POST['title'], text=request.POST['post_text'],
                                               user=request.user)
        else:
            title_value=request.POST['title']
            text_value=request.POST['post_text']
            context['title_value'] = title_value
            context['text_value'] = text_value'''

        # if len(request.POST['title']) > 0 and len(request.POST['post_text']) > 0:
        #    Post.objects.create(title=request.POST['title'], text=request.POST['post_text'], user=request.user)

    return render(request, 'blog/post_list.html', context)


def users_list(request):
    if request.method == 'POST':
        action = request.POST['action']

        if action == 'subscribe':
            request.user.subscribed_on.add(int(request.POST['subscribe_to']))

        elif action == 'unsubscribe':
            request.user.subscribed_on.remove(int(request.POST['unsubscribe_from']))
            removal_post_read = Post.objects.filter(user_id=int(request.POST['unsubscribe_from']))
            request.user.is_read_list.remove(*removal_post_read)

    # users = get_user_model().objects.all()
    users = get_user_model().objects.exclude(id=request.user.id)
    return render(request, 'blog/users_list.html', {'users': users})


def news(request):
    if request.method == 'POST':
        action = request.POST['action']
        if action == 'as_un_read':
            request.user.is_read_list.remove(int(request.POST['as_un_read']))
        if action == 'as_read':
            request.user.is_read_list.add(int(request.POST['as_read']))

    users = request.user.subscribed_on.all()
    posts = Post.objects.filter(user__in=users).order_by('-date_creation')

    return render(request, 'blog/news.html', {'posts': posts})