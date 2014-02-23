from django.conf.urls import patterns, include, url
from django.contrib import admin

from api.v1.urls import urlpatterns as v1_urlpatterns

urlpatterns = patterns('',
    url(r'^v1/',
        include(v1_urlpatterns, namespace='v1')),
    url(r'^auth/', 
        include('rest_framework.urls', namespace='rest_framework')),
)
