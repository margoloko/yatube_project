from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Post, Group


def index(request: HttpRequest) -> HttpResponse:
    ''' Функция выводит на главную страницу десять последних постов'''
    posts = Post.objects.all()[:10]
    template = 'posts/index.html'
    context = {'posts': posts, }
    return render(request, template, context)


def group_posts(request: HttpRequest, slug) -> HttpResponse:
    ''' Функция group_posts передаёт в шаблон posts/group_list.html десять
    последних объектов модели Post, принадлежащих соответствующей группе'''
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {'group': group,
               'posts': posts, }
    return render(request, template, context)
