from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # using include like this roots another URLConf in this position, essentially.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls', namespace='home')),
)
