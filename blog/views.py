from django.shortcuts import render
from blog.models import Post


def post_list(request):
    post=Post.objects.all()
    return render(request, 'index.html', {'post': post})


def order_post(request):
    post=Post.objects.all().order_by('title')
    return render (request, 'order_list.html',{'order_post': post})





