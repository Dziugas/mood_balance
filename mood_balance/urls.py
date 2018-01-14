from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url((r'^about/'), include('about.urls')),
    url((r'^$'), include('home.urls')),
    url((r'^contact/'), include('contact.urls')),
    url((r'^blog/'), include('blog.url'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)