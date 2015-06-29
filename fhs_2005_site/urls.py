from django.conf.urls import patterns, include, url
from django.contrib.auth.views import password_reset
from django.contrib import admin

urlpatterns = patterns('',
    # using include like this roots another URLConf in this position, essentially.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^accounts/password_reset/$',
           password_reset,
           {'html_email_template_name': 'registration/password_reset_email_html.html'},
           name='password_reset',
       ),
    url(r'^accounts/', include('django.contrib.auth.urls')),
)

admin.site.site_header = 'fhs2005.org'
