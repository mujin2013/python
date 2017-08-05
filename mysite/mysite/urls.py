from django.conf.urls import patterns, include, url
from mysite.views import hello,myage
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^myage/$',myage),
    ('^hello/$',hello),
)
