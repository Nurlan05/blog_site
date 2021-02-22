"""djangoprojesi2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')"""
from django.conf.urls import include, url
from django.contrib import admin
from blogSitesi import views

#static ve settings import edirik
from django.conf.urls.static import static

from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.gonderi_listesi, name='gonderi_listesi'),
]

#static ve media fayllarin oxunmasi ucun elave edirik
if settings.DEBUG:
    urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Site  administrasiyası'
admin.site.site_title = 'Site  administrasiyası'
admin.site.index_title = 'Site  administrasiyası'