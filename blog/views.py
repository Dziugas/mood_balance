from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


def blog(request):
    articles = Article.objects.all().order_by('date')
    return render (request, 'blog/blog.html', {'articles': articles})

def article_detail(request, slug):
    article = Article.objects.get(slug = slug)
    return render(request, 'blog/article_detail.html', {'article': article})

def article_create(request):
    return render(request, 'blog/article_create.html')