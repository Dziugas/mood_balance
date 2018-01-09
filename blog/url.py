from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.blog, name='blog')
]


# Create your views here.
