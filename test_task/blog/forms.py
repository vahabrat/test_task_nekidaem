from django.forms import ModelForm

from .models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model=Post
        fields = ['title', 'text',]


    def save(self, user):
        obj = super().save(commit=False)
        obj.user = user
        obj.save()
        return obj
