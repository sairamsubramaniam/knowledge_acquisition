from datetime import datetime
from django import template
from django.conf import settings
from django.shortcuts import (render, redirect, get_object_or_404, get_list_or_404, reverse)
from django.http import (HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect,
                        HttpResponsePermanentRedirect)
from .models import Author, Tag, Post, Category


def index(request):
    return HttpResponse("Hello Django")


def post_list(request):
    posts = Post.objects.order_by("-id").all()
    return render(request, "blog/post_list.html", {"posts":posts})


def post_detail(request, pk, post_slug):
    post = get_object_or_404(Post, pk=pk)
    #try:
        #post = Post.objects.get(pk=pk)
    #except Post.DoesNotExist:
        #return HttpResponseNotFound("Page not found")
        #raise Http404("Post not found")
    return render(request, "blog/post_detail.html", {"post":post})


def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/post_by_category.html', context)


def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context )


def test_redirect(request):
    return redirect(reverse('post_list'), permanent=True)
