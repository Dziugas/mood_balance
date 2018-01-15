from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
]


# Create your views here.
