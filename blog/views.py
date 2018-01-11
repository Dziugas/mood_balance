from django.shortcuts import render
from .models import Article

def blog(request):
    articles = Article.objects.all().order_by('date')
    return render (request, 'blog/blog.html', {'articles': articles})