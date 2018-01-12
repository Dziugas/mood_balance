from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def blog(request):
    articles = Article.objects.all().order_by('date')
    return render (request, 'blog/blog.html', {'articles': articles})

def article_detail(request, slug):
    return HttpResponse(slug)