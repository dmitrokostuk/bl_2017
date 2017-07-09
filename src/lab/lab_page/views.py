from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.contrib.auth import authenticate,login
from django.template import RequestContext
from django.core.paginator import Page, PageNotAnInteger, Paginator, EmptyPage
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post,Travels
from .forms import PostForm,UserForm


def news(request):
    ''' Show all news '''
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 7)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var
    }
    return render(request, 'news/news.html',
                  context)

def regions_list(request):
    travels = Travels.objects.all()
    context = {
        "region_list":travels,
        "title":"List of regions"
    }
    return render(request,'regions_list.html',context)
def home(request):
    ''' Show all news '''
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 7)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var
    }
    return render(request, 'index.html', context)


def news_detail(request, slug=None):
    ''' Show single news'''
    post = get_object_or_404(Post, slug=slug)
    context = {
        "title": post.title,
        "author": post.author,
        "timestamp": post.timestamp,
        "post": post
    }

    return render(request, 'news/one_new.html', context)


def news_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, "Post Created")
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, "news_form.html", context)


def news_update(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, )
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        "title": post.title,
        "post": post,
        "form": form,
    }
    return render(request, "news_form.html", context)


def news_delete(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Post deleted")
    return redirect("news:list")


