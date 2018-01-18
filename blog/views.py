from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


def blog(request):
    articles = Article.objects.all().order_by('date')
    return render (request, 'blog/blog.html', {'articles': articles})

def article_detail(request, slug):
    article = Article.objects.get(slug = slug)
    return render(request, 'blog/article_detail.html', {'article': article})

@login_required(login_url='/accounts/login/')
def article_create(request):
    form = forms.CreateArticle()
    return render(request, 'blog/article_create.html', {'form':form})