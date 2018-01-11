from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url((r'^about/'), include('about.urls')),
    url((r'^$'), include('home.urls')),
    url((r'^contact/'), include('contact.urls')),
    url((r'^blog/'), include('blog.url'))
]

urlpatterns += staticfiles_urlpatterns()