from django.shortcuts import render
from .models import Post


def index(request):
    post = Post.objects.all()

    return render(request, 'index.html', {'post':post})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'post_detail.html', {'post':post})