from django.shortcuts import render

# Create your views here.
# coding: utf8

from django.shortcuts import render, redirect

from post.forms import ArticleForm
from post.forms import CommentForm
from post.models import Article, Comment


def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})


def article(request):
    aid = int(request.GET.get('aid', 0))
    article = Article.objects.get(id=aid)
    comments = article.get_comment()
    return render(request, 'article.html', {'article': article, 'comments': comments})


def editor(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            aid = form.cleaned_data['aid']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            article = Article.objects.get(id=aid)
            article.title = title
            article.content = content
            article.save()
            return redirect('/post/article/?aid=%s' % aid)
        else:
            return redirect('/post/home/')
    else:
        aid = int(request.GET.get('aid', 0))
        article = Article.objects.get(id=aid)
        return render(request, 'editor.html', {'article': article})


def search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        articles = Article.objects.filter(content__contains=keyword)
        return render(request, 'home.html', {'articles': articles})
    return redirect('/post/home/')


def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            aid = form.cleaned_data['aid']
            name = form.cleaned_data['name']
            content = form.cleaned_data['content']
            Comment.objects.create(aid=aid, name=name, content=content)
            return redirect('/post/article/?aid=%s' % aid)
    return redirect('/post/home/')
